import re
from src.system.logging.logger import log


class Validation:
    def __init__(self, regex, error_message):
        self.regex = regex
        self.error_message = error_message


def validate_input(string, validation: Validation = None):
    if is_valid_length(string) is False:
        return False, "Input exceeds maximum length"

    if is_not_empty(string) is False:
        return False, NOT_EMPTY_OR_WHITESPACE.error_message

    if validation:
        if match_regex(validation.regex, string) is False:
            return False, validation.error_message

    return True, None  # string passed all checks


# validation objects, contains regexes and error messages
USERNAME = Validation(
    "^[a-zA-Z][a-zA-Z0-9_'.]{5,10}$",
    "Incorrect username format. username must be between 6 and 10 characters.")

PASSWORD = Validation(
    "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$",
    "Incorrect password format. Password must be between 6 and 30 characters and "
    "must have a combination of at least one lowercase letter, one uppercase letter, "
    "one digit, and one special character such as ~!@#$%&_-+=`|\(){}[]:;'<>,.?/")

PHONE = Validation(
    "^[0-9]{6}$",
    "Incorrect phone format. Format must be DDDDDD")

EMAIL = Validation(
    "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$",
    "Incorrect email format. Example: sample@email.com")

ZIPCODE = Validation(
    "^[0-9]{4}[A-Z]{2}$",
    "Incorrect zipcode format. Format must be DDDDXX")

NOT_EMPTY_OR_WHITESPACE = Validation(
    "^$|\s+",
    "Input is empty. Please enter a valid input")


# check is string is under 255 characters
def is_valid_length(string):
    log("Input exceeded maximum length", "Input by user exceeded maximum length of 255 characters", True)
    return len(string) < 255


def is_not_empty(string):
    return match_regex(NOT_EMPTY_OR_WHITESPACE.regex, string) is False


# utility function for checking whether a string matches a pattern
def match_regex(regex, string):
    pattern = re.compile(regex)
    res = re.match(pattern, string)
    return bool(res)


