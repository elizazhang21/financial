import numpy as np
import pandas as pd
from ..constants import logger
from ..models import DailyTransaction


class Transactions(object):

    def __init__(self):
        self.important_categories = [
            'Food', 'Grocery', 'Bill', 'Apparel', 'Transportation', 'Rent', 'Entertainment', 'Social'
        ]
        self.records = self.get_txn_records()

    def get_txn_records(self):
        logger.info('Fetching all transaction records')
        records = pd.DataFrame(list(
                DailyTransaction.objects.values())
            ).sort_values(
                ['txn_date', 'bank_acct', 'txn_category']
            )[['txn_date', 'bank_acct', 'amount', 'currency', 'txn_category']]
        records['month'] = records['txn_date'].apply(lambda x: x.strftime('%Y-%m'))
        return records

    def calculate_total_consumption(self, records):
        total = pd.DataFrame(records.groupby(['currency']).apply(lambda x: x['amount'].sum()))
        total.rename(columns={0: 'total'}, inplace=True)
        return total

    def calculate_category_consumption(self, records, total, detailed=True):
        if not detailed:
            records = records.copy()
            records['txn_category'] = records['txn_category'].apply(
                lambda x: x if x in self.important_categories else 'Other'
            )

        category = records.groupby(['currency', 'txn_category', 'month']).apply(lambda x: x['amount'].sum())
        category = category.reset_index('txn_category')
        category.rename(columns={0: 'amount'}, inplace=True)

        # get percentage
        df = category.merge(total, left_index=True, right_index=True, how='left')
        df['pct'] = df['amount'] / df['total'] * 100
        return df

    def check_payments(self, records):
        return records.loc[records['txn_category'] == 'Payment', 'amount'].sum() == 0

    def plot(self):
        pass
