from src.system.security.validation import *


def safe_input(label: str = "", validator: Validator = None, default_output=False):
    value = input(label)

    if value == "" and default_output:
        return default_output

    if not is_valid_length(value):
        print("Input exceeded maximum length")
        log("Input exceeded maximum length", "Input by user exceeded maximum length of 255 characters", True)
        return False

    if validator:
        if not validator.check(value):
            print(validator.error_message)
            return False

    return value
