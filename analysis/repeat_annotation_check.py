#!/usr/bin/env python3
"""Recount exact labelled events in the frozen repeat-annotation exercise."""

import argparse
import csv
import hashlib
import json
from collections import Counter
from pathlib import Path


def read_rows(path):
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def event(row):
    return (row["Project"], row["File"], row["Antipattern"],
            int(row["Line from"]), int(row["Line to"]))


def recount(root):
    names = ("files-to-reannotate.csv", "ground-truth.csv",
             "reannotated-ground-truth.csv")
    paths = [root / "datasets" / name for name in names]
    selected, original, repeated = map(read_rows, paths)
    files = {(row["Project"], row["File"]) for row in selected}
    original = [row for row in original if (row["Project"], row["File"]) in files]
    assert all((row["Project"], row["File"]) in files for row in repeated)
    left, right = list(map(event, original)), list(map(event, repeated))
    matches = sum((Counter(left) & Counter(right)).values())

    # Replay notebook 12's span-first pairing to explain its historical diagonal.
    remaining = list(right)
    historical_matches, cross_class_pairs = 0, []
    for reference in left:
        for index, candidate in enumerate(remaining):
            if reference[:2] + reference[3:] == candidate[:2] + candidate[3:]:
                remaining.pop(index)
                if reference[2] == candidate[2]:
                    historical_matches += 1
                else:
                    cross_class_pairs.append({
                        "project": reference[0], "file": reference[1],
                        "line_from": reference[3], "line_to": reference[4],
                        "original_class": reference[2], "repeated_class": candidate[2],
                    })
                break

    negative = files - {row[:2] for row in left}
    still_negative = negative - {row[:2] for row in right}
    classes = sorted({row[2] for row in left + right})
    assert (len(files), len(left), len(right), len(classes)) == (128, 158, 149, 15)
    assert (len(negative), len(still_negative)) == (64, 63)
    assert (matches, historical_matches, len(cross_class_pairs)) == (144, 142, 2)
    return {
        "input_sha256": {path.name: hashlib.sha256(path.read_bytes()).hexdigest()
                         for path in paths},
        "selected_files": len(files), "original_events": len(left),
        "repeated_events": len(right), "observed_classes": classes,
        "original_negative_files": len(negative),
        "still_negative_files": len(still_negative),
        "exact_labelled_matches": matches,
        "precision": matches / len(right), "recall": matches / len(left),
        "f1": 2 * matches / (len(left) + len(right)),
        "historical_span_first_diagonal": historical_matches,
        "historical_cross_class_pairs": cross_class_pairs,
        "method": "Multiset intersection of project, file, class and inclusive span; "
                  "replay of historical span-first pairing for comparison only.",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("study_root", type=Path)
    args = parser.parse_args()
    print(json.dumps(recount(args.study_root), indent=2, sort_keys=True))
