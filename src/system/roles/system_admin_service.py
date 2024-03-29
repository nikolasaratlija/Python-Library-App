from src.system.context import Context
import src.system.backup.backup as backup
from src.system.logging.logger import log
from sqlite3 import IntegrityError

from src.system.repository.users import update_user, get_all_users
from src.system.util.query_builder import base_query_builder


def add_advisor(advisor_username, advisor_pass):
    advisor_username = advisor_username.lower()
    con = Context.db_connection
    c = con.cursor()

    try:
        c.execute("INSERT INTO users (id, username, password, role_id) VALUES (NULL, ?, ?, 3)",
                  (advisor_username, advisor_pass))
        con.commit()
        log("Advisor Added",
            f"Advisor named '{advisor_username}' has been added to the system")
        return True, f"Advisor named '{advisor_username}' has been added to the system"
    except IntegrityError:
        log("Advisor Not Added",
            f"Advisor named '{advisor_username}' is not added to the system")
        return True, f"Error adding advisor. Possibly because username already exists"


def update_advisor(user_id, username, password, role_id):
    return update_user(user_id, username, password, role_id)


def delete_advisor(advisor_id):
    con = Context.db_connection
    c = con.cursor()
    c.execute("DELETE FROM users WHERE id = ? AND role_id = 3", (advisor_id,))

    if c.rowcount == 1:
        con.commit()
        log("Advisor Deleted", f"Advisor '#{advisor_id}' has been deleted from the system")
        return True, f"Advisor '#{advisor_id}' has been removed"
    else:
        log("Advisor Not Deleted", f"Advisor '#{advisor_id}' does not exist")
        return False, f"Advisor '#{advisor_id}' does not exist"


def reset_advisor_password(new_temp_password, advisor_id):
    con = Context.db_connection
    c = con.cursor()
    c.execute("UPDATE users SET password = ? WHERE id = ? AND role_id = 3", (new_temp_password, advisor_id))

    if c.rowcount == 1:
        con.commit()
        log("Reset Password", f"Advisor '#{advisor_id}' has had their password changed")
        return True, f"Advisor '#{advisor_id}' has had their password changed"
    else:
        log("Reset Password", f"Advisor '#{advisor_id}' does not exist")
        return False, f"Advisor '#{advisor_id}' does not exist"


def read_all_users():
    return get_all_users()


def delete_member(member_id):
    con = Context.db_connection
    c = con.cursor()
    c.execute("DELETE FROM members WHERE id = ?", (member_id,))

    if c.rowcount == 1:
        con.commit()
        log("Member Deleted", f"Advisor '#{member_id}' has been deleted from the system")
        return True, f"Member '#{member_id}' has been removed"
    else:
        log("Member Not Deleted", f"Member '#{member_id}' does not exist")
        return False, f"Member '#{member_id}' does not exist"


def create_backup():
    return backup.create_backup()


def restore_backup():
    return backup.restore_backup()


def read_logs():
    try:
        with open('src/system/logging/log.log') as log_file:
            log('Log Read', 'Log file read by member')
            return log_file.read()
    except FileNotFoundError:
        log('read_logs() error', 'Log file could not be found')
        return 'Error: Log file could not be found'


def _read_users_query_builder(search_parameters):
    search_conditions = {
        'id': 'm.id LIKE :id',
        'username': 'username LIKE :username',
        'role': 'r.name LIKE :role',
    }

    sql = "SELECT u.id, username, password, r.name " \
          "FROM users u " \
          "JOIN roles r on u.role_id = r.id"

    return base_query_builder(sql, search_parameters, search_conditions)
