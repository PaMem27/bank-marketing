"""Load campaign records and prepare chronological splits."""

import pandas as pd


NUMERIC_FEATURES = ("age", "previous")
CATEGORICAL_FEATURES = (
    "job", "marital", "education", "default", "housing", "loan", "poutcome",
)


def load_campaign(path):
    return pd.read_csv(path, sep=";")


def split_chronologically(frame):
    """Input rows must already be ordered from oldest to newest."""
    train_end = int(len(frame) * 0.70)
    validation_end = int(len(frame) * 0.85)
    train = frame.iloc[:train_end].copy()
    validation = frame.iloc[train_end:validation_end].copy()
    test = frame.iloc[validation_end:].copy()
    return train, validation, test


def prepare_xy(frame):
    """Select the audited pre-call features and preserve the original row IDs."""
    bad = set(frame["y"].unique()) - {"yes", "no"}
    if bad:
        raise ValueError(f"Unexpected target values: {bad}")
    y = frame["y"].map({"yes": 1, "no": 0})
    X = frame.loc[:, [*NUMERIC_FEATURES, *CATEGORICAL_FEATURES]]
    return X, y
