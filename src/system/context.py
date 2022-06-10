from .roles.advisor import Advisor


# an object which contains different state attributes of the current session
class Context:
    user: Advisor
    role_id: int
