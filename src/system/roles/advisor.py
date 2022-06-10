from src.system.roles.member import Member


class Advisor:
    def update_own_password(self):
        pass

    def add_member(self, member: Member):
        print("TEST FUNCTION\n"
              "Added member with attributes:\n"
              f"{member.first_name}\n"
              f"{member.last_name}\n"
              )

    def modify_member(self):
        pass

    def read_member(self):
        pass
