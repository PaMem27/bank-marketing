import unittest

from bank_marketing.ranking import first_eligible_index, top_k_customers


class RankingTests(unittest.TestCase):
    def test_descending_scores(self):
        customers = [("A", 0.42), ("B", 0.90), ("C", 0.90), ("D", 0.65)]
        self.assertEqual(top_k_customers(customers, 3), ["B", "C", "D"])

    def test_ties_and_budget(self):
        customers = [("Z", 0.90), ("A", 0.90), ("M", 0.65)]
        self.assertEqual(top_k_customers(customers, 1), ["Z"])
        self.assertEqual(top_k_customers(customers, 0), [])
        self.assertEqual(top_k_customers(customers, 5), ["Z", "A", "M"])

    def test_first_eligible_index(self):
        scores = [0.40, 0.60, 0.60, 0.75, 0.90]
        self.assertEqual(first_eligible_index(scores, 0.60), 1)
        self.assertEqual(first_eligible_index(scores, 0.70), 3)
        self.assertEqual(first_eligible_index(scores, 0.95), 5)
        self.assertEqual(first_eligible_index([], 0.60), 0)
