import numpy as np
import pandas as pd

from ..constants import logger
from ..constants import (
    FED_BRACKET, FED_FICA, FED_MEDICARE, FED_DEDUCTION, FED_EXEMPTION,
    STATE_BRACKET, STATE_DEDUCTION, LOCAL_BRACKET, LOCAL_DEDUCTION)

today = pd.Timestamp('today').normalize()


class CashFlow(object):

    def __init__(self, annual_income, monthly_rent, monthly_expense, monthly_consumption, annual_return):
        self.annual_income = annual_income
        self.monthly_rent = monthly_rent
        self.monthly_expense = monthly_expense
        self.monthly_consumption = monthly_consumption
        self.annual_return = annual_return

        # get post-tax income
        self.tax = self.get_tax()
        self.annual_disposable = self.annual_income - self.tax['total']
        self.annual_saving = self.get_saving()

    # # # # # calculate post-tax income
    def get_tax(self):
        # federal tax
        logger.info('Calculating federal tax')
        fed_taxable = self.annual_income - FED_DEDUCTION - FED_EXEMPTION
        fed_tax = self._calculate_tax_bracket(fed_taxable, FED_BRACKET)
        fed_fica = self.annual_income * FED_FICA
        fed_medicare = self.annual_income * FED_MEDICARE

        # state tax
        logger.info('Calculating state tax')
        state_taxable = self.annual_income - STATE_DEDUCTION
        state_tax = self._calculate_tax_bracket(state_taxable, STATE_BRACKET)

        # local tax
        logger.info('Calculating local tax')
        local_taxable = self.annual_income - LOCAL_DEDUCTION
        local_tax = self._calculate_tax_bracket(local_taxable, LOCAL_BRACKET)

        tax = {
            'fed_tax': fed_tax,
            'fed_fica': fed_fica,
            'fed_medicare': fed_medicare,
            'state_tax': state_tax,
            'local_tax': local_tax,
        }
        tax['total'] = sum(tax.values())
        tax['effective'] = tax['total'] / self.annual_income * 100

        return tax

    def _calculate_tax_bracket(self, taxable, bracket):
        df = pd.DataFrame(bracket, columns=['level', 'rate']).sort_values('level')
        df['taxable'] = df.apply(lambda x: min(x['level'], taxable), axis=1)
        df['tax'] = (df['taxable'].diff() * df['rate']).fillna(0)
        tax = df['tax'].sum()
        return tax

    # # # # # calculate saving and investment cashflow
    def get_saving(self):
        saving = self.annual_disposable - (self.monthly_rent + self.monthly_expense + self.monthly_consumption) * 12
        return saving

    def get_capital_growth(self, periods=20):
        logger.info('Projecting capital growth')
        year = pd.date_range(today, freq='AS', periods=periods).strftime('%Y')
        df = pd.DataFrame({'saving': self.annual_saving, 'return': self.annual_return}, index=year)
        df.index.name = 'year'

        df['compound'] = (df['return'] + 1).cumprod()
        df['capital'] = (df['saving'] * df['compound']).cumsum()
        return df[['capital']]

    # # # # # format plot data
    def format_constitution(self, include_tax=True):
        constitution = {
            'rent': self.monthly_rent * 12,
            'expense': self.monthly_expense * 12,
            'consumption': self.monthly_consumption * 12,
            'saving': self.annual_saving,
        }

        if include_tax:
            tax = {k: v for k, v in self.tax.items() if k not in ['effective', 'total']}
            constitution.update(tax)

        df = pd.DataFrame(list(constitution.items()), columns=['item', 'value'])
        df['pct'] = df['value'] / df['value'].sum() * 100
        return df
