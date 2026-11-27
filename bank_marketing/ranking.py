"""Customer ranking and the sorted-score search exercise."""


def top_k_customers(customers, k):
    """Return IDs in descending score order for a nonnegative call budget."""
    ranked = sorted(customers, key=lambda customer: customer[1], reverse=True)
    return [customer_id for customer_id, score in ranked[:k]]


def first_eligible_index(scores, threshold):
    """Find the first score >= threshold in ascending order, or return len(scores)."""
    low, high = 0, len(scores) - 1
    while low <= high:
        middle = low + (high - low) // 2
        if scores[middle] >= threshold:
            high = middle - 1
        else:
            low = middle + 1
    return low
