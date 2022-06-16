import logging
from src.system.context import Context

logging.basicConfig(
    filename='src/system/logging/log.log',
    level=logging.DEBUG,
    format='%(username)s | %(asctime)s | %(description)s | %(message)s | %(suspicious)s',
    datefmt='%d-%m-%Y %I:%M:%S')


def log(description, message, is_suspicious=False):
    log_info = {
        'username': Context.user_name,
        'description': description,
        'suspicious': 'Yes' if is_suspicious else 'No'
    }
    logging.info(message, extra=log_info)
