import numpy as np
import pandas as pd

from ..constants import logger
from ..constants import (
    FED_BRACKET, FED_FICA, FED_MEDICARE, FED_DEDUCTION, FED_EXEMPTION,
    STATE_BRACKET, STATE_DEDUCTION, LOCAL_BRACKET, LOCAL_DEDUCTION)


class CashFlow(object):

    def __init__(
        self, annual_income, income_growth,
        monthly_rent, monthly_expense, monthly_consumption, annual_return
    ):
        self.annual_income = annual_income
        self.monthly_rent = monthly_rent
        self.monthly_expense = monthly_expense
        self.monthly_consumption = monthly_consumption
        self.annual_return = annual_return

    def get_tax(self):
        # federal tax
        fed_taxable = self.annual_income - FED_DEDUCTION - FED_EXEMPTION
        fed_tax = self._calculate_tax_bracket(fed_taxable, FED_BRACKET)
        fed_fica = self.annual_income * FED_FICA
        fed_medicare = self.annual_income * FED_MEDICARE

        # state tax
        state_taxable = self.annual_income - STATE_DEDUCTION
        state_tax = self._calculate_tax_bracket(state_taxable, STATE_BRACKET)

        # local tax
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
