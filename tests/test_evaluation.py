import unittest

import pandas as pd

from bank_marketing.evaluation import evaluate_at_k


class EvaluateAtKTests(unittest.TestCase):
    def test_matches_outcomes_by_row_id_and_breaks_ties_in_score_order(self):
        scores = pd.Series([0.8, 0.8, 0.3, 0.9], index=[32, 14, 20, 11])
        labels = pd.Series([0, 1, 1, 0], index=[14, 11, 32, 20])

        result = evaluate_at_k(scores, labels, 2)

        self.assertEqual(result["selected"], 2)
        self.assertEqual(result["subscribers"], 2)
        self.assertEqual(result["precision"], 1.0)
        self.assertEqual(result["random_subscribers"], 1.0)
        self.assertEqual(result["lift"], 2.0)

    def test_rejects_labels_for_different_rows(self):
        scores = pd.Series([0.8, 0.2], index=[32, 14])
        labels = pd.Series([1, 0], index=[32, 20])

        with self.assertRaisesRegex(ValueError, "same unique row IDs"):
            evaluate_at_k(scores, labels, 1)
