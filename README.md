# Bank Marketing | Before the first call

**The held-out top 100 contained 73 subscribers, versus 38.45 expected from 100 randomly selected records in the same period.** That is **73% precision@100** and **1.90× lift**. A logistic regression model ranked the records using nine customer profile and prior-campaign fields.

The project asks which customers a bank should prioritize when it can make only 100 term-deposit calls. The evaluation is a retrospective benchmark on UCI's historical contact records. The archive lacks customer identifiers and verified first-call snapshots. [Feature audit](docs/feature_audit.md)

| Evaluation period | Records | Subscribers in top 100 | Expected subscribers at random | Lift@100 |
|---|---:|---:|---:|---:|
| Validation | 6,178 | 24 | 10.65 | 2.25× |
| Held-out test | 6,179 | 73 | 38.45 | 1.90× |

Precision@100 is the fraction of selected records with observed subscriptions. Lift@100 divides that precision by the subscription rate in the same period. The model and its preprocessing were fitted on the earliest 28,831 records, using the later periods for evaluation. [Benchmark report](docs/final_report.md)

## Run the project

Use Python 3.11 or 3.12. In the project directory, create and activate a virtual environment, install dependencies, and run the tests.

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
```

1. Download the dataset and extract `bank-additional-full.csv` from `bank-additional.zip` into a local `data` directory. The CSV has 41,188 rows. [UCI Bank Marketing dataset](https://doi.org/10.24432/C5K306)
2. Run `python -m bank_marketing.benchmark` to reproduce the validation and held-out results. The command accepts an optional CSV path.
3. Run `python -m jupyterlab capstone.ipynb` and execute all cells for the full walkthrough. The notebook rebuilds `campaign_train` in `data/bank_marketing.db` from the training split and checks the SQL channel summary against Pandas.

## Project files

| Area | Files |
|---|---|
| Data and feature audit | [Data preparation](bank_marketing/data.py), [scoring-time assumptions](docs/feature_audit.md) |
| Model and evaluation | [Logistic regression](bank_marketing/baselines.py), [ranking metrics](bank_marketing/evaluation.py), [benchmark runner](bank_marketing/benchmark.py) |
| SQL and exploration | [Channel summary](sql/channel_summary.sql), [job summary](sql/job_summary.sql), [notebook](capstone.ipynb) |
| Results and verification | [Benchmark report](docs/final_report.md), [unit tests](tests/) |

## Training-period exploration

The training period contained 1,606 subscriptions across 28,831 records, a rate of 5.57%.

| Training contact channel | Records | Subscriptions | Subscription rate |
|---|---:|---:|---:|
| Cellular | 15,038 | 1,051 | 6.99% |
| Telephone | 13,793 | 555 | 4.02% |

The `student` category had the highest observed subscription rate among jobs with at least 100 training records (33 of 237, or 13.92%). The most common category was `admin.` with 7,107 records. The median age was 39 and the middle half of ages spanned 33 to 47.

The channel and job summaries store `subscription_rate` as a fraction. In the class balance table, `percentage` uses a 0–100 scale.
