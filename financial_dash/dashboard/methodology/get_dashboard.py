from .constants import logger
from .methodology.bal_analysis import Balance


def get_balance_analysis():
    # get balance data
    balance = Balance()
    bal_dict = {}
    for currency in ['CNY', 'USD']:
        bal_dict[currency] = {}
        bal_dict[currency]['data'] = balance.get_last_balance(currency)
        bal_dict[currency]['tv'] = balance.get_total_value(bal_dict[currency]['data'])
        bal_dict[currency]['obs_date'] = bal_dict[currency]['data']['observation_date'].min()

    # get balance plot data

    return bal_dict
