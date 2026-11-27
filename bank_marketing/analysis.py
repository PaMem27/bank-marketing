"""Training-period summaries used by the notebook."""

import pandas as pd


def summarize_channels(train):
    return (
        train.assign(is_yes=train["y"].eq("yes"))
        .groupby("contact", as_index=False, dropna=False)
        .agg(
            n_records=("y", "size"),
            n_subscribed=("is_yes", "sum"),
            subscription_rate=("is_yes", "mean"),
        )
        .sort_values(["subscription_rate", "contact"], ascending=[False, True])
        .reset_index(drop=True)
    )


def class_balance(train):
    summary = train["y"].value_counts().to_frame(name="count")
    summary["percentage"] = 100 * summary["count"] / len(train)
    return summary


def missing_values(train):
    return pd.DataFrame({
        "null_count": train.isna().sum(),
        "unknown_count": train.eq("unknown").sum(),
    })
