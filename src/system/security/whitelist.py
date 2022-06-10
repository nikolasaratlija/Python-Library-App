import re


def validate_input(string, regex=None):
    if is_valid_length(string) is False:
        return False

    if regex:
        if match_regex(regex, string) is False:
            return False

    return True  # string passed all checks


PASSWORD_REGEX = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$"
PHONE_REGEX = "^[0-9]{6}$"
EMAIL_REGEX = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
ZIPCODE_REGEX = "^[0-9]{4}[A-Z]{2}$"


# check is string is under 255 characters
def is_valid_length(string):
    return len(string) < 255


# utility function for checking whether a string matches a pattern
def match_regex(regex, string):
    pattern = re.compile(regex)
    res = re.match(pattern, string)
    return bool(res)
