from src.system.roles.member import Member
from src.system.context import Context


def update_own_password(user_id, new_password):
    password_updated = False
    con = Context.db_connection
    c = con.cursor()

    c.execute("SELECT * FROM users WHERE (id = ? AND role_id = 3)", (user_id,))
    result = c.fetchone()

    if not result:
        c.execute("UPDATE users SET password = ? WHERE (id = ? AND role_id = 3)", (new_password, user_id))
        con.commit()
        # print("Password Updated") #LOG THIS
        password_updated = True
    else:
        # print("No user found to update, entered correct id?") #LOG THIS
        password_updated = False

    return password_updated


def add_member(member: Member):
    # TODO: not finished
    con = Context.db_connection
    c = con.cursor()
    c.execute("INSERT INTO members (first_name, last_name) VALUES (?, ?)",
              (member.first_name, member.last_name))
    con.commit()
    print("Member Added")


def modify_member():
    pass


def read_member(member_id):
    con = Context.db_connection
    c = con.cursor()
    c.execute("SELECT * FROM members WHERE id = ?", (member_id,))
    result = c.fetchone()

    if not result:
        return "User cannot be found!"

    return result
