import pandas as pd
import json

from ..constants import logger


def get_cap_growth_plot(cap_growth):
    logger.info('Plot capital growth')
    plot_data = {}

    plot_data['x_axis'] = cap_growth.index.tolist()
    plot_data['series'] = [{
        'name': 'Capital Growth',
        'data': cap_growth['capital'].tolist(),
    }]
    return plot_data


def get_constitution_plot(cons):
    plot_data = {}
    df = cons.rename(
        columns={
            'item': 'name',
            'value': 'y'
        })[['name', 'y']]

    plot_data = [{
        'name': 'Amount',
        'innerSize': '50%',
        'data': df.to_dict('record')
    }]
    return plot_data
