import logging
import sys
import datetime


class Logger(object):
    def __init__(self):
        logging.basicConfig(
            format='%(asctime)s.%(msecs)03d %(name)s %(levelname)s: %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
            level=logging.DEBUG,
            stream=sys.stdout
        )
        self.logger = logging.getLogger('FINANCIAL_DB')

    def info(self, msg):
        self.logger.info(msg)

    def debug(self, msg):
        self.logger.debug(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

logger = Logger()

# path
year_month = datetime.date.today().strftime('%Y%m')
record_name = 'records/{}.xlsx'.format(year_month)
