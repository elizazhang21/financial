import logging
import sys


class Logger(object):
    def __init__(self):
        logging.basicConfig(
            format='%(asctime)s.%(msecs)03d %(name)s %(levelname)s: %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
            level=logging.DEBUG,
            stream=sys.stdout
        )
        self.logger = logging.getLogger('FINANCIAL_CF')

    def info(self, msg):
        self.logger.info(msg)

    def debug(self, msg):
        self.logger.debug(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

logger = Logger()


# tax brackets
FED_BRACKET = [
    (0, 0),
    (9325, 0.1),
    (37950, 0.15),
    (91900, 0.25),
    (191650, 0.28),
    (416700, 0.33),
    (418400, 0.35),
    (1e8, 0.396),
]

FED_FICA = 0.062
FED_MEDICARE = 0.0145

FED_DEDUCTION = 6350
FED_EXEMPTION = 4050


STATE_BRACKET = [
    (0, 0),
    (8450, 0.04),
    (11650, 0.045),
    (13850, 0.0525),
    (21300, 0.059),
    (80150, 0.0645),
    (214000, 0.0665),
    (1070350, 0.0685),
    (100000000, 0.0882),
]

STATE_DEDUCTION = 7950


LOCAL_BRACKET = [
    (0, 0),
    (12000, 0.02907),
    (25000, 0.03534),
    (50000, 0.03591),
    (500000, 0.03648),
    (1e8, 0.03876),
]

LOCAL_DEDUCTION = 3000
