import pandas as pd
import datetime
from constants import logger

from db_session import start_session, close_session
from db_models import InvestmentCNY, InvestmentUSD
from scrapers import fistrade


def get_investment(currency):
    logger.info('Getting {} investment balance'.format(currency))

    if currency == 'USD':
        pass
    elif currency == 'CNY':
        pass

    return


def write_investment(session, balance, model):
    logger.info('Writing to database: {}'.format(model.__tablename__))
    session.bulk_insert_mappings(model, balance.to_dict('record'))
    session.commit()


if __name__ == '__main__':
    # fetch data and write to database
    session, engine = start_session()
    df_usd = get_investment('USD')
    df_cny = get_investment('CNY')
    write_investment(session, df_usd, InvestmentUSD)
    write_investment(session, df_cny, InvestmentCNY)
    close_session(session)
