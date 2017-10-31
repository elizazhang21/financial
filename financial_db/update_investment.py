import pandas as pd
import datetime
from constants import logger

from db_session import start_session, close_session
from db_models import InvestmentUSD
from scrapers import firstrade, cpwm


def get_investment(currency):
    logger.info('Getting {} investment balance'.format(currency))

    if currency == 'USD':
        inv_firstrade = firstrade.get_balance('Troy')
        inv_firstrade_dc = firstrade.get_balance('Doris')
        # inv_cpwm = cpwm.get_balance()

        df = pd.DataFrame([{
                'account': 'Firstrade',
                'balance': inv_firstrade,
            }, {
                'account': 'Firstrade_DC',
                'balance': inv_firstrade_dc * 6.0 / 7.0,
            }])

    df['observation_date'] = pd.Timestamp('today').date()
    return df


def write_investment(session, balance, model):
    logger.info('Writing to database: {}'.format(model.__tablename__))
    session.bulk_insert_mappings(model, balance.to_dict('record'))
    session.commit()


if __name__ == '__main__':
    # fetch data and write to database
    session, engine = start_session()
    df_usd = get_investment('USD')
    write_investment(session, df_usd, InvestmentUSD)
    close_session(session)
