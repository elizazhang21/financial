import numpy as np
import pandas as pd
from ..constants import logger
from ..models import InvestmentUSD, InvestmentCNY


class Investment(object):

    def __init__(self):
        self.investment_model = {
            'CNY': InvestmentCNY,
            'USD': InvestmentUSD,
        }
