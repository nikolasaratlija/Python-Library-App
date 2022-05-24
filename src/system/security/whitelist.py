import re


def password(input):
    pass


reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$"
match_re = re.compile(reg)

res = re.search(match_re, "asd@Asd1")

if res:
    print("Valid Password")
else:
    print("Invalid Password")
