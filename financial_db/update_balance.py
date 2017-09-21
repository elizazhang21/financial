import pandas as pd
import datetime
from db_session import start_session, close_session, logger
from db_models import (
    DailyTransaction, InvestmentTransfer, Income,
    BalanceCNY, BalanceUSD
)


def get_last_balance(session, currency):
    if currency == 'USD':
        model = BalanceUSD
    elif currency == 'CNY':
        model = BalanceCNY
    else:
        logger.error('Wrong currency!')

    df_query = session.query(model)
    df = pd.read_sql(df_query.statement, df_query.session.bind)
    df = df.sort_values(
            ['observation_date', 'last_update']
        ).drop_duplicates('account', keep='last')
    return df[['observation_date', 'account', 'balance']]


def get_records(session, model):
    logger.info('Fetching records from database: {}'.format(model.__tablename__))
    df_query = session.query(model)
    df = pd.read_sql(df_query.statement, df_query.session.bind)

    if model.__tablename__ == 'income':
        df.rename(columns={'net_income': 'amount'}, inplace=True)
    return df[['txn_date', 'bank_acct', 'amount', 'currency']]


def calculate_change(balance, records, currency):
    logger.info('Calculating changes: {}'.format(records['currency'].unique()[0]))
    filtered = records.loc[records['currency'] == currency]
    merged = filtered.merge(
        balance, left_on='bank_acct', right_on='account', how='left')

    # group by & sum
    df = merged.loc[merged['txn_date'] > merged['observation_date']]
    changes = df[['bank_acct', 'amount']].groupby('bank_acct').sum()
    return changes


def calculate_balance(balance_old, records_dict, currency):
    df = balance_old[['account', 'balance']].copy().set_index('account')

    # calculate changes
    changes_dict = {}
    for key, records in records_dict.items():
        changes_dict[key] = calculate_change(balance_old, records, currency)
        df = df.merge(changes_dict[key], left_index=True, right_index=True, how='outer')
        df.rename(columns={'amount': key}, inplace=True)

    # calculate new balance
    balance_new = pd.DataFrame(
            df.sum(axis=1), columns=['balance']
        ).round(2).reset_index().rename(columns={'index': 'account'})
    balance_new['observation_date'] = datetime.date.today()
    return balance_new


def write_balance(session, balance_new, currency):
    if currency == 'USD':
        model = BalanceUSD
    elif currency == 'CNY':
        model = BalanceCNY
    else:
        logger.error('Wrong currency!')

    logger.info('Writing to database: {}'.format(model.__tablename__))
    session.bulk_insert_mappings(model, balance_new.to_dict('record'))


if __name__ == '__main__':
    session, engine = start_session()

    # get records
    records_dict = {
        'daily_transaction': get_records(session, DailyTransaction),
        'investment_transfer': get_records(session, InvestmentTransfer),
        'income': get_records(session, Income),
    }

    # calculate & save to db
    for currency in ['CNY', 'USD']:
        balance_old = get_last_balance(session, currency)
        balance_new = calculate_balance(balance_old, records_dict, currency)
        write_balance(session, balance_new, currency)
    close_session(session)
