from src.system.security.validation import *


def safe_input(label: str = "", passing_condition=None):
    value = input(label)

    if not is_valid_length(value):
        print("Input exceeded maximum length")
        return False

    if passing_condition:
        if not passing_condition[0](value):
            print(passing_condition[1])
            return False

    return value
