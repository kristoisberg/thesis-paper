#!/usr/bin/env python3
"""Reconstruct the held-out predictions and run robustness checks."""

import argparse
import json
from io import StringIO
from pathlib import Path

import numpy as np
import pandas as pd


KEYS = ["Project", "File", "Antipattern"]
THRESHOLDS = (0.25, 0.50, 0.75, 1.00)


def load_data(artifact_root: Path) -> tuple[pd.DataFrame, pd.DataFrame]:
    notebook_path = artifact_root / "scripts/14-evaluate-tool-localisation.ipynb"
    notebook = json.loads(notebook_path.read_text())
    cell = next(
        cell
        for cell in notebook["cells"]
        if "results_df = pd.concat" in "".join(cell.get("source", []))
    )
    html = "".join(
        next(
            output["data"]["text/html"]
            for output in cell["outputs"]
            if "text/html" in output.get("data", {})
        )
    )
    predictions = pd.read_html(StringIO(html))[0].drop(columns=["Unnamed: 0"])
    reference = pd.read_csv(artifact_root / "datasets/test-set.csv")
    reference["Project"] = reference["Project"].str.replace("/", "_", regex=False)

    for frame in (reference, predictions):
        frame["Antipattern"] = (
            frame["Antipattern"]
            .replace({"Beware of the Unknown": "Fear of the Unknown"})
            .str.replace("’", "'", regex=False)
        )
        for column in KEYS:
            frame[column] = frame[column].str.strip()
        frame["Line from"] = frame["Line from"].astype(int)
        frame["Line to"] = frame["Line to"].astype(int)

    return reference, predictions


def interval_iou(left: tuple[int, int], right: tuple[int, int]) -> float:
    if left[0] > left[1] or right[0] > right[1]:
        return 0.0
    overlap = max(0, min(left[1], right[1]) - max(left[0], right[0]) + 1)
    union = left[1] - left[0] + right[1] - right[0] + 2 - overlap
    return overlap / union


def match_count(
    reference: list[tuple[int, int]],
    predictions: list[tuple[int, int]],
    threshold: float,
) -> int:
    adjacency = []
    for reference_span in reference:
        candidates = [
            (index, interval_iou(reference_span, prediction_span))
            for index, prediction_span in enumerate(predictions)
            if interval_iou(reference_span, prediction_span) >= threshold
        ]
        adjacency.append(
            [
                index
                for index, _ in sorted(
                    candidates,
                    key=lambda item: (-item[1], predictions[item[0]]),
                )
            ]
        )

    owners: dict[int, int] = {}

    def augment(reference_index: int, seen: set[int]) -> bool:
        for prediction_index in adjacency[reference_index]:
            if prediction_index in seen:
                continue
            seen.add(prediction_index)
            if prediction_index not in owners or augment(
                owners[prediction_index], seen
            ):
                owners[prediction_index] = reference_index
                return True
        return False

    return sum(augment(index, set()) for index in range(len(reference)))


def grouped_intervals(frame: pd.DataFrame) -> dict[tuple[str, str, str], list]:
    return {
        key: list(zip(group["Line from"], group["Line to"], strict=True))
        for key, group in frame.groupby(KEYS, sort=True)
    }


def event_counts(
    reference: pd.DataFrame,
    predictions: pd.DataFrame,
    threshold: float,
) -> tuple[list[str], list[str], np.ndarray]:
    reference_groups = grouped_intervals(reference)
    prediction_groups = grouped_intervals(predictions)
    keys = sorted(reference_groups.keys() | prediction_groups.keys())
    projects = sorted({key[0] for key in keys})
    classes = sorted({key[2] for key in keys})
    project_index = {project: index for index, project in enumerate(projects)}
    class_index = {name: index for index, name in enumerate(classes)}
    counts = np.zeros((len(projects), len(classes), 3), dtype=int)

    for key in keys:
        reference_spans = reference_groups.get(key, [])
        prediction_spans = prediction_groups.get(key, [])
        true_positives = match_count(reference_spans, prediction_spans, threshold)
        counts[project_index[key[0]], class_index[key[2]]] += (
            true_positives,
            len(prediction_spans) - true_positives,
            len(reference_spans) - true_positives,
        )

    return projects, classes, counts


def metrics(counts: np.ndarray) -> tuple[float, float, float]:
    true_positives, false_positives, false_negatives = counts
    precision = true_positives / (true_positives + false_positives)
    recall = true_positives / (true_positives + false_negatives)
    f1 = 2 * true_positives / (2 * true_positives + false_positives + false_negatives)
    return precision, recall, f1


def print_sensitivity(reference: pd.DataFrame, predictions: pd.DataFrame) -> np.ndarray:
    primary_counts = None
    print("## IoU sensitivity\n")
    print("| IoU | TP | FP | FN | Precision | Recall | F1 |")
    print("|---:|---:|---:|---:|---:|---:|---:|")
    for threshold in THRESHOLDS:
        _, _, counts = event_counts(reference, predictions, threshold)
        totals = counts.sum(axis=(0, 1))
        precision, recall, f1 = metrics(totals)
        print(
            f"| {threshold:.2f} | {totals[0]} | {totals[1]} | {totals[2]} "
            f"| {precision:.3f} | {recall:.3f} | {f1:.3f} |"
        )
        if threshold == 0.50:
            primary_counts = counts

    assert primary_counts is not None
    assert primary_counts.sum(axis=(0, 1)).tolist() == [460, 76, 63]
    return primary_counts


def bootstrap(
    classes: list[str],
    counts: np.ndarray,
    iterations: int,
    seed: int,
) -> None:
    rng = np.random.default_rng(seed)
    sample = rng.integers(0, counts.shape[0], size=(iterations, counts.shape[0]))
    sampled_counts = counts[sample].sum(axis=1)

    def metric_samples(values: np.ndarray) -> np.ndarray:
        with np.errstate(divide="ignore", invalid="ignore"):
            precision = values[:, 0] / (values[:, 0] + values[:, 1])
            recall = values[:, 0] / (values[:, 0] + values[:, 2])
            f1 = 2 * values[:, 0] / (
                2 * values[:, 0] + values[:, 1] + values[:, 2]
            )
        return np.column_stack((precision, recall, f1))

    print(f"\n## Project bootstrap at IoU 0.50\n")
    print(f"Iterations: {iterations}; seed: {seed}.\n")
    print("| Result | Metric | Point | 2.5% | 97.5% | Defined replicates |")
    print("|---|---|---:|---:|---:|---:|")

    rows = [("Micro", counts.sum(axis=(0, 1)), sampled_counts.sum(axis=1))]
    rows.extend(
        (name, counts[:, index].sum(axis=0), sampled_counts[:, index])
        for index, name in enumerate(classes)
    )
    for name, point_counts, samples in rows:
        point = metrics(point_counts)
        sampled_metrics = metric_samples(samples)
        for index, metric_name in enumerate(("Precision", "Recall", "F1")):
            values = sampled_metrics[:, index]
            values = values[np.isfinite(values)]
            lower, upper = np.quantile(values, (0.025, 0.975))
            print(
                f"| {name} | {metric_name} | {point[index]:.3f} | {lower:.3f} "
                f"| {upper:.3f} | {len(values)}/{iterations} |"
            )


def main() -> None:
    assert interval_iou((2, 1), (1, 1)) == 0.0
    parser = argparse.ArgumentParser()
    parser.add_argument("artifact_root", type=Path)
    parser.add_argument("--bootstrap", type=int, default=10_000)
    parser.add_argument("--seed", type=int, default=20_260_827)
    args = parser.parse_args()

    reference, predictions = load_data(args.artifact_root)
    projects, classes, primary_counts = event_counts(reference, predictions, 0.50)
    print(
        f"Reconstructed {len(predictions)} predictions and {len(reference)} reference "
        f"occurrences from {len(projects)} projects.\n"
    )
    checked_counts = print_sensitivity(reference, predictions)
    assert np.array_equal(primary_counts, checked_counts)
    bootstrap(classes, primary_counts, args.bootstrap, args.seed)


if __name__ == "__main__":
    main()
