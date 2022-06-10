class Member:
    def __init__(self,
                 first_name,
                 last_name,
                 zip_code=None,
                 city=None,
                 email=None,
                 phone=None):
        self.phone = phone
        self.email = email
        self.city = city
        self.zip_code = zip_code
        self.last_name = last_name
        self.first_name = first_name
