"""Fit the logistic regression baseline using the audited features."""

from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from .data import CATEGORICAL_FEATURES, NUMERIC_FEATURES


def fit_logistic_regression(features, labels):
    preprocessing = ColumnTransformer([
        ("numeric", StandardScaler(), list(NUMERIC_FEATURES)),
        ("categorical", OneHotEncoder(handle_unknown="ignore"), list(CATEGORICAL_FEATURES)),
    ])
    model = make_pipeline(preprocessing, LogisticRegression(solver="lbfgs", C=1.0, max_iter=1000))
    return model.fit(features, labels)
