import logging
import os

from src.system.context import Context
from src.system.logging.logger import log
import src.system.security.encryption as encryption


def close_application():
    log("Closing Application", "Closing Application: Starting shutdown sequence")

    _close_services()

    _encrypt_files()

    _delete_files()


def _encrypt_files():
    # encrypt database and log files before deletion
    log("Shutdown: Encrypt", "Closing Application: Encrypted database and log")
    encryption.encrypt_all_files()


def _close_services():
    # close database
    Context.db_connection.close()
    log("Shutdown: Database", "Closing Application: Database connection closed")

    # disable logger
    logging.shutdown()
    logging.getLogger().handlers.clear()
    log("Shutdown: Log", "Closing Application: Shutting down logger component")


def _delete_files():
    # delete log file
    try:
        log("Shutdown: Delete Log", "Closing Application: Removing unencrypted logger")
        os.remove(encryption.LOG_FILE)
    except OSError as e:
        print(e)
        log("Shutdown: Log ERROR", "Cannot remove log file")

    # delete database file
    try:
        log("Shutdown: Delete Database", "Closing Application: Removing unencrypted database")
        os.remove(encryption.DATABASE_FILE)
    except OSError as e:
        print(e)
        log("Shutdown: Delete Log ERROR", "Cannot remove database file")
