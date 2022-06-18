import re
from src.system.logging.logger import log

# validation objects, contains regexes and error messages
is_digit = (
    lambda string: match_regex("^[0-9]+$", string), "ERROR: Input must be an integer.")

is_username = (
    lambda string: match_regex("^[a-zA-Z][a-zA-Z0-9_'.]{5,10}$", string),
    "Error: Incorrect username format. username must be between 6 and 10 characters.")

is_password = (
    lambda string: match_regex("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$", string),
    "Error: Incorrect password format. Password must be between 6 and 30 characters and "
    "must have a combination of at least one lowercase letter, one uppercase letter, "
    "one digit, and one special character such as ~!@#$%&_-+=`|\(){}[]:;'<>,.?/")

is_phone_number = (
    lambda string: match_regex("^[0-9]{6}$", string), "Error: Incorrect phone format. Format must be DDDDDD")

is_email = (
    lambda string: match_regex("^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$", string),
    "Error: Incorrect email format. Example: sample@email.com")

is_zipcode = (
    lambda string: match_regex("^[0-9]{4}[A-Z]{2}$", string),
    "Error: Incorrect zipcode format. Format must be DDDDXX")

not_empty = (
    lambda string: string,
    "Error: Input is empty. Please enter a valid input")


# check is string is under 255 characters
def is_valid_length(string):
    log("Input exceeded maximum length", "Input by user exceeded maximum length of 255 characters", True)
    return len(string) < 255


# utility function for checking whether a string matches a pattern
def match_regex(regex, string):
    pattern = re.compile(regex)
    res = re.match(pattern, string)
    return bool(res)
