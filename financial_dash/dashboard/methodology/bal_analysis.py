import numpy as np
import pandas as pd
from ..constants import logger
from ..models import BalanceUSD, BalanceCNY


class Balance(object):

    def __init__(self):
        self.balance_model = {
            'CNY': BalanceCNY,
            'USD': BalanceUSD,
        }

    def get_last_balance(self, currency):
        balance = pd.DataFrame(list(
                self.balance_model[currency].objects.values())
            ).sort_values(
                ['account', 'observation_date', 'last_update']
            ).drop_duplicates('account', keep='last')

        # calculate total value & percentage
        balance['pct'] = balance['balance'] / balance['balance'].sum()
        return balance[['account', 'observation_date', 'balance', 'pct']]

    def get_total_value(self, balance):
        return balance['balance'].sum().round(2)

    def plot_last_balance(self, currency):
        pass
