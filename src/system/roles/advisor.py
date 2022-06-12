from src.system.roles.member import Member
from src.database.connection import get_connection


class Advisor:
    def update_own_password(self):
        pass

    def add_member(self, member: Member):
        # TODO: not finished
        con = get_connection()
        c = con.cursor()
        c.execute("INSERT INTO member (first_name, last_name) VALUES (?, ?)",
                  (member.first_name, member.last_name))
        con.commit()
        con.close()
        print("Member Added")


    def modify_member(self):
        pass

    def read_member(self):
        pass
