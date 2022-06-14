from src.database.connection import get_connection


def add_advisor(advisor_id, advisor_username, advisor_pass):
    con = get_connection()
    c = con.cursor()
    c.execute("INSERT INTO users (id, username, password, role_id) VALUES (?, ?, ?, 3)",(advisor_id, advisor_username, advisor_pass))
    con.commit()
    con.close()
    print("Advisor Added")


def modify_advisor():
    pass


def delete_advisor(advisor_id):
    con = get_connection()
    c = con.cursor()
    c.execute("DELETE FROM users WHERE id = ? AND role_id = 3",(advisor_id,))
    con.commit()
    con.close()
    print("Advisor Deleted")


def reset_advisor_password(new_temp_password, advisor_id):
    con = get_connection()
    c = con.cursor()
    c.execute("UPDATE users SET password = ? WHERE id = ? AND role_id = 3",(new_temp_password, advisor_id))
    con.commit()
    con.close()
    print("Password Updated")


def read_all_users():
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT username, r.name "
              "FROM users u "
              "LEFT JOIN roles r on u.role_id = r.id")
    members = c.fetchall()
    conn.close()
    return members


def delete_member(member_id):
    con = get_connection()
    c = con.cursor()
    c.execute("DELETE FROM members WHERE id = ?",(member_id,))
    con.commit()
    con.close()
    print("Member Deleted")


def backup():
    pass


def read_logs():
    pass
