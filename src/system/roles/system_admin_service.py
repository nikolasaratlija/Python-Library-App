from src.system.context import Context
import src.system.backup.backup as backup
from src.system.logging.logger import log
from sqlite3 import IntegrityError


def add_advisor(advisor_username, advisor_pass):
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
        return True, f"Error adding advisor. Possibly because username already exists"


def modify_advisor():
    pass


def delete_advisor(advisor_id):
    con = Context.db_connection
    c = con.cursor()
    c.execute("DELETE FROM users WHERE id = ? AND role_id = 3", (advisor_id,))

    if c.rowcount == 1:
        con.commit()
        log("Advisor Deleted", f"Advisor '#{advisor_id}' has been deleted from the system")
        return True, f"Advisor '#{advisor_id}' has been removed"
    else:
        return False, f"Advisor '#{advisor_id}' does not exist"


def reset_advisor_password(new_temp_password, advisor_id):
    con = Context.db_connection
    c = con.cursor()
    c.execute("UPDATE users SET password = ? WHERE id = ? AND role_id = 3", (new_temp_password, advisor_id))
    con.commit()
    print("Password Updated")


def read_all_users(search_parameters):
    con = Context.db_connection
    c = con.cursor()

    sql, params = _read_users_query_builder(search_parameters)
    c.execute(sql, params)

    members = c.fetchall()
    return members


def delete_member(member_id):
    con = Context.db_connection
    c = con.cursor()
    c.execute("DELETE FROM members WHERE id = ?", (member_id,))

    if c.rowcount == 1:
        con.commit()
        log("Member Deleted", f"Advisor '#{member_id}' has been deleted from the system")
        return True, f"Member '#{member_id}' has been removed"
    else:
        return False, f"Member '#{member_id}' does not exist"


def create_backup():
    return backup.create_backup()


def restore_backup():
    return backup.restore_backup()


def read_logs():
    try:
        with open('src/system/logging/log.log') as log_file:
            log('Log file read by member', 'Log file read by member')
            return log_file.read()
    except FileNotFoundError:
        log('read_logs() error', 'Log file could not be found')
        return 'Error: Log file could not be found'


def _read_users_query_builder(search_parameters):
    # TODO TRY CATCH
    search_conditions = {
        'id': 'm.id LIKE :id',
        'username': 'username LIKE :username',
        'role': 'r.name LIKE :role',
    }

    sql = "SELECT u.id, username, password, r.name " \
          "FROM users u " \
          "JOIN roles r on u.role_id = r.id"

    conditions = []
    params = {}

    for key, value in search_parameters.items():
        if key in search_conditions:
            conditions.append(search_conditions[key])
            params[key] = '%' + search_parameters[key] + '%'

    where_statement = ' AND '.join(conditions)
    sql += " WHERE " + where_statement
    return sql, params
