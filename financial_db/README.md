## Personal Financial Statement Database

#### DB list

- cny asset balance
- use asset balance
- daily transaction entries
- cny investment balance
- usd investment balance
- investment transfer entries

#### DB structure

##### daily transaction entries

1. txn_date
2. bank_acct: bank account that is involved in the transaction
3. amount
4. currency
5. txn_category
6. last_update
7. description: detailed description for the transaction, nullable

##### investment transfer entries

1. txn_date
2. bank_acct
3. inv_acct
4. amount
5. currency
6. last_update
7. description