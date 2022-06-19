from src.system.context import Context
from sqlite3 import IntegrityError
from src.system.util.query_result_formatter import format_query_result


def get_advisor(advisor_id):
    return get_user(advisor_id, 3)


def get_admin(admin_id):
    return get_user(admin_id, 2)


def get_user(user_id, role_id):
    con = Context.db_connection
    c = con.cursor()
    c.execute("SELECT * FROM users WHERE id = ? AND role_id = ?", (user_id, role_id))

    user = c.fetchone()

    if not user:
        return None

    return format_query_result(c.description, user)


def update_user(user_id, username, password, role_id):
    con = Context.db_connection
    c = con.cursor()

    try:
        c.execute(
            "UPDATE users "
            "SET    username = ?,"
            "       password = ?,"
            "       role_id = ? "
            "WHERE id = ?"
            , (username, password, role_id, user_id))

        if c.rowcount == 1:
            con.commit()
            return True, "User updated."
        else:
            return False, "Error: Could not update user."

    except IntegrityError as e:
        return False, "This username already exists"
