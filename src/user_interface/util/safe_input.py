from src.system.security.validation import *


def safe_input(label: str = "", validator: Validator = None):
    value = input(label)

    if not is_valid_length(value):
        print("Input exceeded maximum length")
        return False

    if validator:
        if not validator.check(value):
            print(validator.error_message)
            return False

    return value
