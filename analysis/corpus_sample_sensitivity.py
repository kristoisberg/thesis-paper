#!/usr/bin/env python3
"""Compare pooled corpus flag measures by annotation-sample membership."""

import csv
import sys
from collections import Counter
from pathlib import Path

from corpus_normalization import format_rate


def read_rows(name):
    with Path(__file__).with_name(name).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def main():
    source_rows = read_rows("corpus_phase2_by_repository.csv")
    partition_rows = read_rows("split_file_counts_by_repository.csv")
    annotated = {row["repository"] for row in partition_rows}
    assert len(annotated) == len(partition_rows) == 61
    assert Counter(row["split"] for row in partition_rows) == {
        "training": 21, "validation": 20, "test": 20
    }

    broad = "Any retained class [broad detector-output density]"
    corpus = {row["repository"] for row in source_rows if row["analysis_label"] == broad}
    assert len(corpus) == 602 and annotated <= corpus
    remaining = corpus - annotated
    assert len(remaining) == 541 and not (remaining & annotated)
    assert remaining | annotated == corpus

    labels = (
        "ID Required [generated schema]",
        "Implicit Columns [application/query source]",
        broad,
    )
    fields = ("eligible_files", "flagged_files", "flags")
    groups = (("annotated", annotated), ("remaining", remaining), ("full", corpus))
    writer = csv.writer(sys.stdout, lineterminator="\n")
    writer.writerow(("subset", "repositories", "analysis_label", *fields,
                     "breadth_percent", "flags_per_flagged_file", "flags_per_100_eligible_files",
                     "generated_schema_flags", "application_query_flags"))
    for label in labels:
        rows = [row for row in source_rows if row["analysis_label"] == label]
        assert len(rows) == len(corpus) and {row["repository"] for row in rows} == corpus
        counts = []
        for name, members in groups:
            selected = [row for row in rows if row["repository"] in members]
            eligible, flagged, flags = totals = tuple(
                sum(int(row[field]) for row in selected) for field in fields
            )
            counts.append(totals)
            role_flags = ("", "")
            if label == broad:
                by_role = Counter()
                for row in source_rows:
                    if row["repository"] in members and row["analysis_label"] != broad:
                        by_role[row["eligible_source_role"]] += int(row["flags"])
                role_flags = (by_role["generated schema"], by_role["application/query source"])
                assert sum(role_flags) == flags
            writer.writerow((name, len(members), label, *totals,
                             format_rate(flagged, eligible, 100),
                             format_rate(flags, flagged),
                             format_rate(flags, eligible, 100), *role_flags))
        assert tuple(a + b for a, b in zip(*counts[:2])) == counts[2]


if __name__ == "__main__":
    main()
