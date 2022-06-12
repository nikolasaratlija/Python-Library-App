import re


class Validation:
    def __init__(self, regex, error_message):
        self.regex = regex
        self.error_message = error_message


def validate_input(string, validation: Validation = None):
    if is_valid_length(string) is False:
        return False

    if validation:
        if match_regex(validation.regex, string) is False:
            return False, validation.error_message

    return True  # string passed all checks

# validation objects, contains regexes and error messages
PASSWORD = Validation(
    "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$",
    "Incorrect password, format must be TODO")

PHONE = Validation(
    "^[0-9]{6}$",
    "Incorrect phone format. Format must be DDDDDD")

EMAIL = Validation(
    "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$",
    "Incorrect email format. Format must be TODO")

ZIPCODE = Validation(
    "^[0-9]{4}[A-Z]{2}$",
    "Incorrect zipcode format. Format must be DDDDXX")


# check is string is under 255 characters
def is_valid_length(string):
    # TODO: Log suspicious activity
    return len(string) < 255


# utility function for checking whether a string matches a pattern
def match_regex(regex, string):
    pattern = re.compile(regex)
    res = re.match(pattern, string)
    return bool(res)
