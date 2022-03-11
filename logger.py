import logging
import sys


def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    console_handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(asctime)s - [%(filename)s:%(lineno)s - %(funcName)s() ] - %(levelname)s\n%(message)s')
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    return logger
