import pandas as pd
import datetime
from db_session import start_session, close_session, logger
from db_models import DailyTransaction, InvestmentTransfer, Income
from constants import record_name


def get_records(db_name):
    logger.info('Getting data from Excel file: {}'.format(db_name))
    df = pd.read_excel(record_name, sheetname=db_name, date_parser='txn_date').dropna(how='all')

    return df


def write_records(session, records, model):
    logger.info('Deleting outdated entries......')
    session.query(model).filter(
        model.txn_date >= datetime.date.today().replace(day=1)).delete()

    logger.info('Writing to database......')
    session.bulk_insert_mappings(model, records.to_dict('record'))


if __name__ == '__main__':
    # fetch data and write to database
    session, engine = start_session()
    for model in [DailyTransaction, InvestmentTransfer, Income]:
        records = get_records(model.__tablename__)
        write_records(session, records, model)

    close_session(session)
