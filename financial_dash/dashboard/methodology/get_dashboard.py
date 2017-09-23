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
        bal_dict[currency]['data'] = balance.get_last_balance(currency)
        bal_dict[currency]['tv'] = balance.calculate_total_value(bal_dict[currency]['data'])
        bal_dict[currency]['obs_date'] = bal_dict[currency]['data']['observation_date'].min()

    return bal_dict


def get_txn_analysis():
    # get transaction analysis
    logger.info('Analyzing transaction records......')
    txn = Transactions()
    txn_dict = {}

    total = txn.calculate_total_consumption(txn.records)
    category_detail = txn.calculate_total_consumption(txn.records, detailed=True)
    category = txn.calculate_total_consumption(txn.records, detailed=False)
    payment_balance = txn.check_payments(txn.records)

    txn_dict['total'] = total
    txn_dict['category_detail'] = category_detail
    txn_dict['category'] = txn.calculate_percentage(category, total)
    txn_dict['payment_balance'] = payment_balance

    return txn_dict
