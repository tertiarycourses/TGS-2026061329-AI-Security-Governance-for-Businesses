# customer-training-data.csv — Data Dictionary
200 fictional NovaBank retail customer records. **Proposed use:** train a churn-prediction model
(target = `churned_flag`) to drive retention campaigns.

| # | Field | Type | Description | Your classification | Keep / Drop / Transform | Method |
|---|---|---|---|---|---|---|
| 1 | customer_id | ID | Internal pseudonymous key | | | |
| 2 | nric | String | National Registration Identity Card number | | | |
| 3 | full_name | String | Full name | | | |
| 4 | first_name | String | Given name | | | |
| 5 | last_name | String | Family name | | | |
| 6 | email | String | E-mail address | | | |
| 7 | mobile | String | Mobile number | | | |
| 8 | address | String | Residential address | | | |
| 9 | postal_code | String | 6-digit postal code | | | |
| 10 | date_of_birth | Date | Date of birth | | | |
| 11 | gender | Category | M / F | | | |
| 12 | ethnicity | Category | Chinese / Malay / Indian / Others | | | |
| 13 | religion | Category | Declared religion | | | |
| 14 | marital_status | Category | Marital status | | | |
| 15 | monthly_income_sgd | Numeric | Declared monthly income | | | |
| 16 | employment_status | Category | Employment status | | | |
| 17 | health_insurance_flag | Y/N | Holds a health insurance product | | | |
| 18 | tenure_months | Numeric | Months as a customer | | | |
| 19 | primary_product_code | Category | Main product held | | | |
| 20 | products_held | Numeric | Count of products | | | |
| 21 | avg_balance_sgd | Numeric | 90-day average balance | | | |
| 22 | txn_count_90d | Numeric | Transactions in last 90 days | | | |
| 23 | preferred_channel | Category | Most-used channel | | | |
| 24 | churned_flag | Y/N | **TARGET** — closed all products in the period | | | |

## Classification key
- **Direct identifier** — identifies an individual on its own
- **Quasi-identifier** — can re-identify in combination with others
- **Sensitive attribute** — special-category or high-harm data
- **Non-personal** — behavioural/product data that does not identify

## The minimisation question
For each field ask ONE question: *does the churn model actually need this to predict churn?*
Expect to drop at least eight fields. Note especially which fields create discrimination risk
if the model learns from them, even where they are legally usable.

## Retention and deletion — complete after your classification
- Training set retained for: ____________
- On a customer deletion request, what happens to the training set: ____________
- On a customer deletion request, what happens to the trained model: ____________
- Where the audit record of this decision lives: ____________
