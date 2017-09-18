import sys
import pandas as pd
import datetime
from db_session import start_session, close_session
from db_models import DailyTransaction, InvestmentTransfer, Income
from constants import record_name, Logger
logger = Logger()


def get_records(db_name, update=False):
    logger.info('Getting data from Excel file: {}'.format(db_name))
    df = pd.read_excel(record_name, sheetname=db_name, date_parser='txn_date').dropna(how='all')

    # update rule: replace most recent 7 days' records
    if update:
        df = df.loc[df['txn_date'] >= datetime.date.today() - datetime.timedelta(7)]

    return df


def write_records(session, records, model, update=False):
    logger.info('Deleting outdated entries......')
    if not update:
        session.query(model).filter(
            model.txn_date >= datetime.date.today().replace(day=1)).delete()
    else:
        session.query(model).filter(
            model.txn_date >= datetime.date.today() - datetime.timedelta(7)).delete()

    logger.info('Writing to database......')
    session.bulk_insert_mappings(model, records.to_dict('record'))


if __name__ == '__main__':
    if 'create' in sys.argv:
        update = False
    elif 'update' in sys.argv:
        update = True
    else:
        logger.error('Please specify "create" or "update"')
        sys.exit(0)

    # fetch data and write to database
    session, engine = start_session()
    for model in [DailyTransaction, InvestmentTransfer, Income]:
        records = get_records(model.__tablename__, update=update)
        write_records(session, records, model, update=update)

    close_session(session)
