#!/usr/bin/env python3
"""Recount the preserved project splits without executing model requests."""

import argparse
import csv
import glob
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

import corpus_normalization as corpus


SPLITS = {"training": 21, "validation": 20, "test": 20}
SUCCESS = re.compile(r"\[\d+/\d+\] File analyzed successfully: (.+)")


def read_csv(path):
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def logged_validation_files(path):
    notebook = json.loads(path.read_text(encoding="utf-8"))
    paths = []
    for cell in notebook["cells"]:
        for output in cell.get("outputs", []):
            text = output.get("text", [])
            text = text if isinstance(text, str) else "".join(text)
            for filename in SUCCESS.findall(text):
                repository, relative = filename.split("/repositories/", 1)[1].split("/", 1)
                paths.append((repository, relative.strip()))
    return paths


def recount(repositories, thesis, frozen_manifest, output):
    digest = corpus.rule_digest(corpus.rule_values())
    assert digest == corpus.EXPECTED_RULE_SHA256, "corpus selection rules changed"
    notebooks = [thesis / "scripts" / name for name in corpus.NOTEBOOKS]
    backups = sorted((thesis / "scripts/backups").glob("09-evaluate-prompting-strategy-*.ipynb"))
    assert len(backups) == 16, f"expected 16 validation copies, found {len(backups)}"
    for path in notebooks + backups:
        values = corpus.notebook_values(path)
        assert {key: values[key] for key in corpus.RULE_NAMES} == corpus.rule_values(), path
    allowlist = thesis / "datasets/final-repositories-corrected.csv"
    allowed = set(corpus.read_allowlist(allowlist))
    membership, annotations, inputs = {}, {}, [allowlist, frozen_manifest, *notebooks, *backups]
    for split, expected in SPLITS.items():
        path = thesis / f"datasets/{split}-set.csv"
        rows = read_csv(path)
        projects = sorted({row["Project"] for row in rows})
        assert len(projects) == expected, (split, len(projects))
        assert set(projects) <= allowed, f"{split} contains a project outside the frozen corpus"
        for project in projects:
            assert project not in membership, f"project overlaps splits: {project}"
            membership[project] = split
        annotations[split] = rows
        inputs.append(path)
    directories = {name.replace("/", "_") for name in membership}
    assert len(directories) == len(membership), "repository directory-name collision"
    frozen = read_csv(frozen_manifest)
    frozen_keys = [(row["repository"], row["relative_path"]) for row in frozen]
    assert len(frozen_keys) == len(set(frozen_keys)) == corpus.EXPECTED_UNIQUE_FILES
    expected_rows = {
        (row["repository"], row["relative_path"]): row
        for row in frozen if row["repository"] in membership
    }
    manifest, projects, duplicate_matches = [], [], []
    for name, split in sorted(membership.items()):
        project = repositories / name.replace("/", "_")
        assert project.is_dir(), f"missing snapshot: {project}"
        selected, broad = {}, Counter()
        for filename in glob.glob(str(project / "**/*.java"), recursive=True):
            path = Path(filename)
            relative = path.relative_to(project).as_posix()
            if relative not in selected:
                selected[relative] = corpus.source_row(name, project, path)
            if selected[relative] is not None:
                broad[relative] += 1
        selected = {key: row for key, row in selected.items() if row is not None}
        narrow = Counter(
            Path(filename).relative_to(project).as_posix()
            for filename in glob.glob(str(project / "**/src/**/*.java"), recursive=True)
            if Path(filename).relative_to(project).as_posix() in selected
        )
        assert set(narrow) == {path for path in selected if "src" in Path(path).parts}
        for relative, row in sorted(selected.items()):
            expected = expected_rows.get((name, relative))
            assert expected is not None, f"new selected file absent from frozen frame: {name}/{relative}"
            assert all(str(value) == expected[key] for key, value in row.items()), f"source changed: {name}/{relative}"
            manifest.append({"split": split, **row})
        for pattern, matches in [("**/*.java", broad), ("**/src/**/*.java", narrow)]:
            for relative, count in sorted(matches.items()):
                if count > 1:
                    duplicate_matches.append({"split": split, "repository": name, "relative_path": relative,
                                              "glob": pattern, "matches": count})
        projects.append({
            "split": split, "repository": name, "relevant_files": len(selected),
            "recursive_glob_matches": sum(broad.values()),
            "src_glob_matches": sum(narrow.values()), "distinct_src_files": len(narrow),
            "duplicate_src_matches": sum(narrow.values()) - len(narrow),
            "files_outside_src": len(selected) - len(narrow),
            "generated_schema_files": sum(row["source_role"] == "generated schema" for row in selected.values()),
            "application_query_files": sum(row["source_role"] == "application/query source" for row in selected.values()),
            "unique_file_contents": len({row["sha256"] for row in selected.values()}),
        })
    actual_keys = {(row["repository"], row["relative_path"]) for row in manifest}
    assert actual_keys == set(expected_rows), "split reconstruction omitted frozen files"
    summaries, annotation_exceptions = [], []
    for split, expected in SPLITS.items():
        rows = [row for row in manifest if row["split"] == split]
        project_rows = [row for row in projects if row["split"] == split]
        hashes = Counter(row["sha256"] for row in rows)
        annotated = {(row["Project"], row["File"]) for row in annotations[split]}
        split_keys = {(row["repository"], row["relative_path"]) for row in rows}
        missing = annotated - split_keys
        for name, relative in sorted(missing):
            path = repositories / name.replace("/", "_") / relative
            annotation_exceptions.append({
                "split": split, "repository": name, "relative_path": relative,
                "source_file_exists": path.is_file(),
                "excluded_path_fragments": ";".join(part for part in corpus.EXCLUDED_PATH_FRAGMENTS if part in relative),
                "reference_events": sum(row["Project"] == name and row["File"] == relative for row in annotations[split]),
            })
        summaries.append({
            "split": split, "repositories": expected, "reference_events": len(annotations[split]),
            "annotated_files": len(annotated),
            "annotated_files_outside_source_frame": len(missing),
            **{key: sum(row[key] for row in project_rows) for key in [
                "relevant_files", "recursive_glob_matches", "src_glob_matches", "distinct_src_files",
                "duplicate_src_matches", "files_outside_src", "generated_schema_files", "application_query_files"]},
            "unique_file_contents": len(hashes),
            "exact_duplicate_groups": sum(count > 1 for count in hashes.values()),
            "files_in_exact_duplicate_groups": sum(count for count in hashes.values() if count > 1),
            "extra_exact_copies": len(rows) - len(hashes),
        })
    validation = {(row["repository"].replace("/", "_"), row["relative_path"])
                  for row in manifest if row["split"] == "validation"}
    archived = {}
    for path in backups:
        logged = logged_validation_files(path)
        assert logged and len(logged) == len(set(logged)), f"missing or duplicate completed-file records: {path}"
        assert set(logged) == validation, f"archived validation frame differs: {path}"
        archived[path.name] = {"completed_files": len(logged), "matches_reconstructed_validation": True}
    by_content = defaultdict(list)
    for row in manifest:
        by_content[row["sha256"]].append(row)
    cross_split = [dict(row, content_group_size=len(rows),
                        content_group_splits=";".join(sorted({r["split"] for r in rows})))
                   for rows in by_content.values() if len({row["split"] for row in rows}) > 1
                   for row in rows]
    output.mkdir(parents=True, exist_ok=True)
    tables = {
        "split_source_manifest.csv": (manifest, ("split", *corpus.MANIFEST_FIELDS)),
        "split_file_counts.csv": (summaries, tuple(summaries[0])),
        "split_file_counts_by_repository.csv": (projects, tuple(projects[0])),
        "split_duplicate_glob_matches.csv": (duplicate_matches, ("split", "repository", "relative_path", "glob", "matches")),
        "split_annotation_frame_exceptions.csv": (annotation_exceptions, ("split", "repository", "relative_path", "source_file_exists", "excluded_path_fragments", "reference_events")),
        "split_cross_partition_exact_duplicates.csv": (sorted(cross_split, key=lambda row: (row["sha256"], row["split"], row["repository"], row["relative_path"])),
                                                       ("split", *corpus.MANIFEST_FIELDS, "content_group_size", "content_group_splits")),
    }
    for filename, (rows, fields) in tables.items():
        corpus.write_csv(output / filename, fields, rows)
    summary = {
        "passed": True, "selection_rule_sha256": digest,
        "method": "Detector **/*.java discovery and original path/content filters; count each repository-relative path once. Exact-content copies remain distinct in the primary count.",
        "source_snapshot": str(repositories), "splits": summaries,
        "archived_validation_runs": archived,
        "cross_split_exact_duplicate_groups": len({row["sha256"] for row in cross_split}),
        "cross_split_exact_duplicate_files": len(cross_split),
        "checks": {"projects_are_disjoint": True, "all_projects_in_frozen_corpus": True,
                   "fresh_source_frame_matches_frozen_manifest": True,
                   "annotation_source_frame_checked": True,
                   "all_annotations_in_source_frame": not annotation_exceptions,
                   "all_16_archived_validation_inventories_match": True},
        "sha256": {"inputs": {str(path): corpus.sha256(path) for path in inputs},
                   "outputs": {name: corpus.sha256(output / name) for name in tables}},
    }
    (output / "split_file_inventory_summary.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"splits": summaries, "cross_split_exact_duplicate_groups": summary["cross_split_exact_duplicate_groups"]}, indent=2))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repositories", type=Path)
    parser.add_argument("thesis", type=Path)
    parser.add_argument("--manifest", type=Path, default=Path("analysis/corpus_source_manifest.csv"))
    parser.add_argument("--output-dir", type=Path, default=Path("analysis"))
    args = parser.parse_args()
    recount(args.repositories, args.thesis, args.manifest, args.output_dir)


if __name__ == "__main__":
    main()
