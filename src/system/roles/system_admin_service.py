from src.system.context import Context
import src.system.backup.backup as backup
from src.system.logging.logger import log


def add_advisor(advisor_id, advisor_username, advisor_pass):
    con = Context.db_connection
    c = con.cursor()
    c.execute("INSERT INTO users (id, username, password, role_id) VALUES (?, ?, ?, 3)",
              (advisor_id, advisor_username, advisor_pass))
    con.commit()
    print("Advisor Added")


def modify_advisor():
    pass


def delete_advisor(advisor_id):
    con = Context.db_connection
    c = con.cursor()
    c.execute("DELETE FROM users WHERE id = ? AND role_id = 3", (advisor_id,))
    con.commit()
    print("Advisor Deleted")


def reset_advisor_password(new_temp_password, advisor_id):
    con = Context.db_connection
    c = con.cursor()
    c.execute("UPDATE users SET password = ? WHERE id = ? AND role_id = 3", (new_temp_password, advisor_id))
    con.commit()
    print("Password Updated")


def read_all_users():
    con = Context.db_connection
    c = con.cursor()
    c.execute("SELECT username, r.name "
              "FROM users u "
              "LEFT JOIN roles r on u.role_id = r.id")
    members = c.fetchall()
    return members


def delete_member(member_id):
    con = Context.db_connection
    c = con.cursor()
    c.execute("DELETE FROM members WHERE id = ?", (member_id,))
    con.commit()
    print("Member Deleted")


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
