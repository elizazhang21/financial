import pandas as pd
import datetime
from ..constants import logger
from .bal_analysis import Balance
from .txn_analysis import Transactions


def get_balance_analysis():
    # get balance analysis
    logger.info('Analyzing asset balances......')
    balance = Balance()
    bal_dict = {}
    for currency in ['CNY', 'USD']:
        bal_dict[currency] = {}
        bal_dict[currency]['data'] = balance.balance_last[currency].to_dict('record')
        bal_dict[currency]['tv'] = balance.calculate_total_value(balance.balance_last[currency])
        bal_dict[currency]['obs_date'] = balance.balance_last[currency]['observation_date'].min()

    return bal_dict


def get_transaction_analysis():
    # get transaction analysis
    logger.info('Analyzing transaction records......')
    txn = Transactions()
    txn_dict = {}

    # get total number and whether payments balanced
    total = txn.calculate_total_consumption(txn.records)
    payment_balance = txn.check_payments(txn.records)

    # consumption by category
    category_detail = txn.calculate_category_consumption(txn.records, total, detailed=True)
    category = txn.calculate_category_consumption(txn.records, total, detailed=False)

    # format dictionary
    txn_dict['total'] = total.to_dict('index')
    txn_dict['payment_balance'] = payment_balance
    txn_dict['category_detail'] = {}
    txn_dict['category'] = {}
    for currency in ['CNY', 'USD']:
        txn_dict['category_detail'][currency] = category_detail.loc[
                (currency, datetime.date.today().strftime('%Y-%m'))
            ].set_index('txn_category').to_dict('index')
        txn_dict['category'][currency] = category.loc[currency].reset_index().to_dict('record')

    return txn_dict
