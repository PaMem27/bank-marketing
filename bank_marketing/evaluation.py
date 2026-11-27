"""Evaluate a ranked contact list against uniform random selection."""

from .ranking import top_k_customers


def evaluate_at_k(scores, labels, k):
    """Score the top k rows, matching scores and outcomes by unique row ID."""
    if k < 1 or scores.empty:
        raise ValueError("Evaluation requires a positive call budget and at least one score")
    if not (
        scores.index.is_unique
        and labels.index.is_unique
        and len(scores) == len(labels)
        and scores.index.isin(labels.index).all()
    ):
        raise ValueError("Scores and labels must cover the same unique row IDs")

    selected_ids = top_k_customers(scores.items(), k)
    selected_count = len(selected_ids)
    subscribers = int(labels.loc[selected_ids].sum())
    precision = subscribers / selected_count
    random_precision = float(labels.mean())
    return {
        "records": len(labels),
        "period_subscribers": int(labels.sum()),
        "selected": selected_count,
        "subscribers": subscribers,
        "precision": precision,
        "random_subscribers": selected_count * random_precision,
        "random_precision": random_precision,
        "lift": precision / random_precision if random_precision else float("nan"),
    }
