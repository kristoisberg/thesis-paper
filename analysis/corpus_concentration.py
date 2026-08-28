#!/usr/bin/env python3
"""Calculate top-decile repository concentration from corpus detector flags."""

import argparse
import csv
import hashlib
import math
from collections import Counter, defaultdict
from pathlib import Path


FROZEN_SHA256 = "76e900ef1ccb2442c9721587bcb96440c564befc608bcd0c1754cca40c64c8b6"
CLASS_ORDER = (
    "Implicit Columns",
    "ID Required",
    "Keyless Entry",
    "Fear of the Unknown",
    "31 Flavors",
    "Poor Man's Search Engine",
    "Rounding Errors",
)
EXPECTED = {
    "Implicit Columns": (7289, 535, 54.6),
    "ID Required": (3597, 523, 59.9),
    "Keyless Entry": (2153, 200, 66.0),
    "Fear of the Unknown": (1256, 205, 56.8),
    "31 Flavors": (390, 87, 52.8),
    "Poor Man's Search Engine": (583, 114, 44.6),
    "Rounding Errors": (663, 86, 63.3),
    "Any retained class": (15931, 601, 59.1),
}


def summarise(counts):
    flagged = len(counts)
    k = math.ceil(flagged * 0.10)
    flags = sum(counts.values())
    share = round(100 * sum(sorted(counts.values(), reverse=True)[:k]) / flags, 1)
    return flags, flagged, k, share


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("csv", type=Path, help="frozen datasets/analysis-results.csv")
    parser.add_argument("--verify-frozen", action="store_true")
    args = parser.parse_args()

    if args.verify_frozen:
        digest = hashlib.sha256(args.csv.read_bytes()).hexdigest()
        if digest != FROZEN_SHA256:
            raise SystemExit(f"unexpected SHA-256: {digest}")

    by_class = defaultdict(Counter)
    overall = Counter()
    with args.csv.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            by_class[row["Antipattern"]][row["Project"]] += 1
            overall[row["Project"]] += 1

    rows = [(name, *summarise(by_class[name])) for name in CLASS_ORDER]
    rows.append(("Any retained class", *summarise(overall)))
    if args.verify_frozen:
        for name, flags, projects, _, share in rows:
            assert (flags, projects, share) == EXPECTED[name]

    print("class,flags,flagged_repositories,top_decile_repositories,top_decile_share")
    for row in rows:
        print(",".join(map(str, row)))


if __name__ == "__main__":
    main()
