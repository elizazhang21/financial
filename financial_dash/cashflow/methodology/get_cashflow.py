import pandas as pd

from ..constants import logger
from .cf_analysis import CashFlow


def get_cashflow(annual_income, monthly_rent, monthly_expense, monthly_consumption, annual_return, periods=20):
    cf = CashFlow(annual_income, monthly_rent, monthly_expense, monthly_consumption, annual_return)
    cf_data = {}

    # render numbers
    cf_data['tax'] = cf.tax
    cf_data['disposable'] = cf.annual_disposable

    # get plot data
    cap_growth = cf.get_capital_growth(periods=periods)
    cons_pre_tax = cf.format_constitution(include_tax=True)
    cons_post_tax = cf.format_constitution(include_tax=False)

    cf_data['cap_growth'] = cap_growth
    cf_data['cons_pre_tax'] = cons_pre_tax
    cf_data['cons_post_tax'] = cons_post_tax

    return cf_data
