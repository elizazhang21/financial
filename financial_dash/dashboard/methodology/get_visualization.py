import pandas as pd
from ..constants import logger


def get_txn_plot(txn_category):
    logger.info('Fetching transaction visualization')
    plot_data = {}
    for currency, records in txn_category.items():
        df = pd.DataFrame(records)
        df = df.rename(columns={
            'txn_category': 'name',
            'pct': 'y',
        })[['name', 'y']]

        plot_data[currency] = [{
            'name': currency,
            'innerSize': '50%',
            'data': df.to_dict('record')
        }]
    return plot_data
