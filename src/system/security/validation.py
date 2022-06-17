import re


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
    # TODO: Log suspicious activity
    return len(string) < 255


def is_not_empty(string):
    return match_regex(NOT_EMPTY_OR_WHITESPACE.regex, string) is False


# utility function for checking whether a string matches a pattern
def match_regex(regex, string):
    pattern = re.compile(regex)
    res = re.match(pattern, string)
    return bool(res)
