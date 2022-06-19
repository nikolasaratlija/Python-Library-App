import logging
import os

from src.system.context import Context
from src.system.logging.logger import log
import src.system.security.encryption as encryption


def close_application():
    log("Closing Application", "Closing Application: Starting shutdown sequence")

    _encrypt_files()

    _shutdown_database()

    _shutdown_logger()


def _encrypt_files():
    # encrypt database and log files before deletion
    log("Shutdown: Encrypt", "Closing Application: Encrypted database and log")
    encryption.encrypt_all_files()


def _shutdown_logger():
    # disable logger
    logging.shutdown()
    logging.getLogger().handlers.clear()
    # no more actions can be logged because the logger has been disabled

    # delete log file
    try:
        os.remove(encryption.LOG_FILE)
    except OSError as e:
        print(e)


def _shutdown_database():
    # close database
    Context.db_connection.close()
    log("Shutdown: Database", "Closing Application: Database connection closed")

    # delete database file
    try:
        log("Shutdown: Delete Database", "Closing Application: Removing unencrypted database")
        os.remove(encryption.DATABASE_FILE)
    except OSError as e:
        print(e)
        log("Shutdown: Delete Log ERROR", "Cannot remove database file")
