# Feature availability before the first call

The intended scoring point is before a customer's first call of the current campaign. The benchmark uses a fixed list of nine inputs from `bank-additional-full.csv`. Customer attributes are assumed to come from a profile available at scoring time. The archive supplies no snapshot timestamps to verify that assumption.

| Fields | Decision | Rationale |
|---|---|---|
| `age`, `job`, `marital`, `education`, `default`, `housing`, `loan` | Include | These are customer profile fields. Preserve `unknown` as a category so the model can use records with missing profile information. |
| `previous`, `poutcome` | Include | The data dictionary defines these as the count of contacts before the current campaign and the previous campaign outcome. Keep `nonexistent` as a category for the absence of a previous campaign outcome. |
| `pdays` | Exclude | `999` denotes no previous contact. The archived day counts lack a verified first-call reference date. |
| `contact`, `month`, `day_of_week` | Exclude | These describe the last recorded contact. The archive has no pre-call schedule or channel plan. |
| `duration` | Exclude | Call duration is observed after the call. |
| `campaign` | Exclude | The recorded count includes contacts made during the current campaign, including the last contact. The count at the intended decision point would be zero. |
| `emp.var.rate`, `cons.price.idx`, `cons.conf.idx`, `euribor3m`, `nr.employed` | Exclude | The archive lacks the publication timestamps and historical vintages needed to establish what was available before the first call. |
| `y` | Target | The observed term-deposit subscription outcome is kept separately from the model features. |

The dataset contains historical contacts. Some clients received multiple calls, and the file lacks customer identifiers for deduplication or verifying customer separation across periods. The benchmark ranks recorded rows using pre-call proxies. Its results describe the concentration of observed subscribers in those rows. Estimating the effect of a new calling policy would require a pre-call eligible population and a prospective comparison.

Field definitions come from `bank-additional-names.txt` in the `bank-additional.zip` archive. [UCI Bank Marketing dataset](https://doi.org/10.24432/C5K306)
