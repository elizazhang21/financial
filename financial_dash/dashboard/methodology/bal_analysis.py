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
        self.balance_last = {
            'CNY': self.get_last_balance('CNY'),
            'USD': self.get_last_balance('USD'),
        }

    def get_last_balance(self, currency):
        logger.info('Fetching latest balance data: {}'.format(currency))
        balance = pd.DataFrame(list(
                self.balance_model[currency].objects.values())
            ).sort_values(
                ['account', 'observation_date', 'last_update']
            ).drop_duplicates('account', keep='last')

        # calculate total value & percentage
        balance['pct'] = balance['balance'] / balance['balance'].sum()
        return balance[['account', 'observation_date', 'balance', 'pct']]

    def get_all_balance(self, currency):
        logger.info('Fetching all balance data: {}'.format(currency))
        balance = pd.DataFrame(list(
                self.balance_model[currency].objects.values())
            ).sort_values(
                ['account', 'observation_date', 'last_update']
            ).drop_duplicates(['account', 'observation_date'], keep='last')

        # choose only week end entries

        return balance

    def calculate_total_value(self, balance):
        return balance['balance'].sum().round(2)

    def plot_last_balance(self, balance):
        pass
