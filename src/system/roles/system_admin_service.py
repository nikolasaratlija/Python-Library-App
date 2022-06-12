from src.database.connection import get_connection


def add_advisor():
    pass


def modify_advisor():
    pass


def delete_advisor():
    pass


def reset_advisor_password():
    pass


def read_all_users():
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT username, r.name "
              "FROM users u "
              "LEFT JOIN roles r on u.role_id = r.id")
    members = c.fetchall()
    conn.close()
    return members


def delete_member():
    pass


def backup():
    pass


def read_logs():
    pass
