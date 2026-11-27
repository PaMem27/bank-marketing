"""Run the chronological 100-call benchmark from the command line or notebook."""

import argparse
from pathlib import Path

import pandas as pd

from .baselines import fit_logistic_regression
from .data import load_campaign, prepare_xy, split_chronologically
from .evaluation import evaluate_at_k


CALL_BUDGET = 100


def run_benchmark(train, validation, test):
    train_features, train_labels = prepare_xy(train)
    model = fit_logistic_regression(train_features, train_labels)

    results = {}
    for period, frame in (("Validation", validation), ("Held-out test", test)):
        features, labels = prepare_xy(frame)
        scores = pd.Series(model.predict_proba(features)[:, 1], index=features.index)
        results[period] = evaluate_at_k(scores, labels, CALL_BUDGET)
    return pd.DataFrame.from_dict(results, orient="index").rename_axis("period")


def format_results(results):
    return results.to_string(formatters={
        "precision": "{:.2%}".format,
        "random_subscribers": "{:.2f}".format,
        "random_precision": "{:.2%}".format,
        "lift": "{:.2f}x".format,
    })


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv", nargs="?", type=Path, default=Path("data/bank-additional-full.csv"))
    args = parser.parse_args()

    splits = split_chronologically(load_campaign(args.csv))
    print(format_results(run_benchmark(*splits)))


if __name__ == "__main__":
    main()
