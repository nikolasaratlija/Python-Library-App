from src.system.roles.member import Member
from src.database.connection import get_connection


def update_own_password():
    pass


def add_member(member: Member):
    # TODO: not finished
    con = get_connection()
    c = con.cursor()
    c.execute("INSERT INTO members (first_name, last_name) VALUES (?, ?)",
              (member.first_name, member.last_name))
    con.commit()
    con.close()
    print("Member Added")


def modify_member():
    pass


def read_member(member_id):
    #TODO: not finished, need to test and see return
    con = get_connection()
    c = con.cursor()
    c.execute("SELECT * FROM members WHERE id = ?", (member_id,))
    result = c.fetchone()
    con.close()
    return result
