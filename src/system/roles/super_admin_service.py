from src.system.context import Context
from src.system.logging.logger import log
from sqlite3 import IntegrityError


def add_admin(system_admin_name, system_admin_pass):
    con = Context.db_connection
    c = con.cursor()

    try:
        c.execute("INSERT INTO users (id, username, password, role_id) VALUES (NULL, ?, ?, 2)",
                  (system_admin_name, system_admin_pass))

        con.commit()
        log("System Admin Added",
            f"System admin named '{system_admin_name}' has been added to the system")
        return True, f"System admin named '{system_admin_name}' has been added to the system"

    except IntegrityError:
        return False, f"System admin with name: '{system_admin_name}' already exists. Please try another name."


def modify_admin():
    pass


def delete_admin(admin_id):
    con = Context.db_connection
    c = con.cursor()
    c.execute("DELETE FROM users WHERE id = ? AND (role_id = 1 OR role_id = 2)", (admin_id,))

    if c.rowcount == 1:
        con.commit()
        log("Admin Deleted", f"System admin '#{admin_id}' has been deleted from the system")
        return True, f"System admin '#{admin_id}' has been removed"
    else:
        return False, f"System admin '#{admin_id}' does not exist"


def reset_admin_password(new_temp_password, admin_id):
    con = Context.db_connection
    c = con.cursor()
    c.execute("UPDATE users SET password = ? WHERE id = ? AND (role_id = 1 OR role_id = 2)",
              (new_temp_password, admin_id))

    if c.rowcount == 1:
        con.commit()
        log("Print Password", f"System admin '#{admin_id}' has had their password changed")
        return True, f"System admin '#{admin_id}' has had their password changed"
    else:
        return False, f"System admin '#{admin_id}' does not exist"
