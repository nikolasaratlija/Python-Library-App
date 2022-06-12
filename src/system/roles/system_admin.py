from .advisor import Advisor
from src.database.connection import get_connection


class SystemAdmin(Advisor):
    def add_advisor(self):
        pass

    def modify_advisor(self):
        pass

    def delete_advisor(self):
        pass

    def rest_advisor_password(self):
        pass

    def read_all_users(self):
        # TODO: not finished
        conn = get_connection()
        c = conn.cursor()
        c.execute("SELECT * FROM member")
        members = c.fetchall()
        for member in members:
            print(f"{member[0]}, {member[1]}, {member[2]}\n")

    def delete_member(self):
        pass

    def backup(self):
        pass

    def read_logs(self):
        pass
