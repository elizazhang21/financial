import pandas as pd

from ..constants import logger
from ..models import DailyTransaction


class Transactions(object):

    def __init__(self):
        self.important_categories = [
            'Food', 'Grocery', 'Bill', 'Apparel', 'Transportation', 'Rent', 'Entertainment', 'Social'
        ]
        self.all_records = self.get_txn_records()
        self.records = self.all_records[
            self.all_records['txn_date'] >=
            pd.Timestamp('today').date().replace(day=1)]
        self.total = self.calculate_total_consumption()

    def get_txn_records(self):
        logger.info('Fetching all transaction records')
        records = pd.DataFrame(list(
            DailyTransaction.objects.values())).sort_values(
                ['txn_date', 'bank_acct', 'txn_category']
            )[['txn_date', 'bank_acct', 'amount', 'currency', 'txn_category']]
        records['month'] = records['txn_date'].apply(lambda x: x.strftime('%Y-%m'))
        return records

    def calculate_total_consumption(self):
        total = pd.DataFrame(self.records.groupby(['currency']).apply(lambda x: x['amount'].sum()))
        total.rename(columns={0: 'total'}, inplace=True)
        return total

    def calculate_category_consumption(self, records, detailed=False):
        df_records = records.copy()
        if not detailed:
            df_records['txn_category'] = df_records['txn_category'].apply(
                lambda x: x if x in self.important_categories else 'Other')

        category = df_records.groupby(['currency', 'txn_category', 'month']).apply(lambda x: x['amount'].sum())
        category = category.reset_index('txn_category')
        category.rename(columns={0: 'amount'}, inplace=True)

        # get percentage
        df = category.merge(self.total, left_index=True, right_index=True, how='left')
        df['pct'] = df['amount'] / df['total'] * 100
        return df

    def check_payments(self):
        return self.records.loc[self.records['txn_category'] == 'Payment', 'amount'].sum() == 0

    def format_hist_plot(self):
        df = self.calculate_category_consumption(self.all_records, detailed=False)
        df = df[df['amount'] <= 0][['txn_category', 'amount']].reset_index()
        df['amount'] = df['amount'].abs()

        plot_data = {}
        for currency in df['currency'].unique():
            df_cur = df[df['currency'] == currency][['month', 'txn_category', 'amount']]
            df_pivot = df_cur.pivot_table(
                index='month', columns='txn_category', values='amount').fillna(0).sort_index()
            plot_data[currency] = {
                'x_axis': list(df_pivot.index.values),
                'data_series': [
                    {'name': key, 'data': value}
                    for key, value in df_pivot.to_dict('list').items()]}
        return plot_data
