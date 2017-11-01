import pandas as pd

from ..constants import logger
from ..models import InvestmentUSD, InvestmentCNY


class Investment(object):

    def __init__(self):
        self.investment_model = {
            'CNY': InvestmentCNY,
            'USD': InvestmentUSD,
        }
        self.investment_last = {
            'CNY': self.get_last_investment('CNY'),
            'USD': self.get_last_investment('USD'),
        }

    def get_last_investment(self, currency):
        logger.info('Fetching latest investment data: {}'.format(currency))
        investment = pd.DataFrame(list(
                self.investment_model[currency].objects.values())
            ).sort_values(
                ['account', 'observation_date', 'last_update']
            ).drop_duplicates('account', keep='last')

        # calculate total value & percentage
        investment['pct'] = investment['balance'] / investment['balance'].sum() * 100
        return investment[['account', 'observation_date', 'balance', 'pct']]

    def calculate_total_value(self, investment):
        return investment['balance'].sum()
