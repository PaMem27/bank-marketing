# Bank marketing benchmark

## Design

The benchmark uses the 41,188 chronological rows in UCI's `bank-additional-full.csv`. It fits one logistic regression pipeline on rows 0–28,830, evaluates validation on rows 28,831–35,008, and evaluates the held-out test on rows 35,009–41,187. These are zero-based positions in the source file. The corresponding subscription rates were 5.57%, 10.65%, and 38.45%.

The pipeline standardizes `age` and `previous` and one-hot encodes the seven categorical fields in the [feature audit](feature_audit.md). It learns the scaling and category vocabulary from the training period. An unseen category produces all zeros for that field. Logistic regression uses L2 regularization with `C=1.0` and the `lbfgs` solver. The same fitted model scores both later periods, with no hyperparameter tuning or refitting.

Each evaluation ranks the rows by predicted subscription probability and selects the first 100. Ties follow the original file order. The random baseline is the expected number of subscribers in a uniform sample of 100 rows without replacement, calculated as 100 times the period's subscription rate. Precision@100 is the fraction of selected rows with observed subscriptions. Lift@100 divides that precision by the same period's subscription rate.

## Results

| Period | Records | Observed subscribers in period | Subscribers in top 100 | Precision@100 | Expected subscribers at random | Lift@100 |
|---|---:|---:|---:|---:|---:|---:|
| Validation | 6,178 | 658 | 24 | 24.00% | 10.65 | 2.25× |
| Held-out test | 6,179 | 2,376 | 73 | 73.00% | 38.45 | 1.90× |

The held-out top 100 contained more subscribers than validation's top 100. Relative to each period's random baseline, lift fell from 2.25× to 1.90× as the underlying subscription rate rose from 10.65% to 38.45%.

The benchmark measures ranking performance on historical contacts with known outcomes. The archive lacks customer IDs and verified first-call snapshots, so repeat contacts or customers can affect the comparison. The period-level change in subscription rate also limits how much to infer about performance in a future campaign. See the [feature audit](feature_audit.md) for the assumptions about scoring-time availability.

## Reproduce

With the CSV at `data/bank-additional-full.csv`, run `python -m bank_marketing.benchmark` from the project directory, or run all cells in [the notebook](../capstone.ipynb). The command-line results were verified with Python 3.12, scikit-learn 1.6.1, and Pandas 2.2.3 and 3.1.0.
