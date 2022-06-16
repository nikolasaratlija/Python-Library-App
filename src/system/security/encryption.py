""" An encryption mechanism based on the Caesar Cypher technique """

_KEY = 5  # 'secret' key for the caesar cypher

_DATABASE_FILE = 'src/database/database.db'
_DATABASE_FILE_ENCRYPTED = 'src/database/ENCRYPTED-database.db'

_LOG_FILE = 'src/system/logging/log.log'
_LOG_FILE_ENCRYPTED = 'src/system/logging/ENCRYPTED-log.log'


def decrypt_files():
    _shift_file(_LOG_FILE_ENCRYPTED, _LOG_FILE)  # decrypt log
    _shift_file(_DATABASE_FILE_ENCRYPTED, _DATABASE_FILE)  # decrypt database


def encrypt_files():
    _shift_file(_LOG_FILE, _LOG_FILE_ENCRYPTED)  # encrypt log file
    _shift_file(_DATABASE_FILE, _DATABASE_FILE_ENCRYPTED)  # encrypt database


def _shift_file(file, new_file_name):
    byte_list = _read_file_as_bytes(file)
    _write_bytes_to_file(new_file_name, byte_list)


def _read_file_as_bytes(filename):
    file = open(f"{filename}", "rb")
    byte_list = file.read()
    file.close()
    return _byte_shift(byte_list)


def _byte_shift(byte_list):
    # perform bitwise operation to shift bytes
    return [value ^ _KEY for index, value in enumerate(byte_list)]


def _write_bytes_to_file(filename, byte_list):
    file = open(f"{filename}", "wb+")
    file.write(bytearray(byte_list))
    file.close()
