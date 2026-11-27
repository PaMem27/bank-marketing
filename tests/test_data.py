import unittest

import pandas as pd

from bank_marketing.data import prepare_xy


class PrepareXYTests(unittest.TestCase):
    def test_rejects_invalid_label(self):
        frame = pd.DataFrame({"age": [30, 45], "duration": [60, 90], "y": ["yes", "yess"]})
        with self.assertRaisesRegex(ValueError, "yess"):
            prepare_xy(frame)

    def test_valid_input(self):
        frame = pd.DataFrame(
            {
                "age": [30, 45],
                "job": ["admin.", "student"],
                "marital": ["married", "single"],
                "education": ["university.degree", "unknown"],
                "default": ["no", "unknown"],
                "housing": ["yes", "no"],
                "loan": ["no", "no"],
                "previous": [0, 1],
                "poutcome": ["nonexistent", "failure"],
                "duration": [60, 90],
                "campaign": [1, 2],
                "pdays": [999, 6],
                "contact": ["telephone", "cellular"],
                "month": ["may", "jun"],
                "day_of_week": ["mon", "tue"],
                "euribor3m": [4.9, 4.8],
                "y": ["yes", "no"],
            },
            index=[12, 27],
        )
        X, y = prepare_xy(frame)
        self.assertEqual(y.tolist(), [1, 0])
        self.assertEqual(X.columns.tolist(), [
            "age", "previous", "job", "marital", "education", "default", "housing", "loan", "poutcome",
        ])
        self.assertEqual(X["age"].tolist(), [30, 45])
        self.assertEqual(X["education"].tolist(), ["university.degree", "unknown"])
        self.assertEqual(X.index.tolist(), [12, 27])
        self.assertEqual(y.index.tolist(), [12, 27])
