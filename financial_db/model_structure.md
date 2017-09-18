## Personal Financial Statement Database

#### DB list

- cny asset balance
- use asset balance
- daily transaction entries
- cny investment balance
- usd investment balance
- investment transfer entries
- income entries

#### DB structure

##### daily transaction entries

1. txn_date
2. bank_acct: bank account that is involved in the transaction
3. amount
4. currency
5. txn_category
6. description: detailed description for the transaction, nullable
7. last_update

##### investment transfer entries

1. txn_date
2. bank_acct
3. inv_acct
4. amount
5. currency
6. description
7. last_update

##### income entries

1. txn_date
2. bank_acct
3. gross_income
4. tax_paid
5. net_income
6. currency
7. description
8. last_update