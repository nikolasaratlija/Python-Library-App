import sqlite3
from src.system.logging.logger import log


def get_connection():
    try:
        return sqlite3.connect('file:src/database/database.db?mode=rw', uri=True)
    except sqlite3.OperationalError as e:
        log('Fatal Database Error',
            'An error occurred while trying to establish a database connection in \'get_connection()\'')
        exit("FATAL ERROR: Could not connect to the database, possibly because it's missing or corrupt.")
