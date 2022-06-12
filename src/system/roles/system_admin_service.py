from src.database.connection import get_connection


def add_advisor():
    pass


def modify_advisor():
    pass


def delete_advisor():
    pass


def rest_advisor_password():
    pass


def read_all_users():
    # TODO: try catch
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM member")
    members = c.fetchall()
    conn.close()
    return members


def delete_member():
    pass


def backup():
    pass


def read_logs():
    pass
