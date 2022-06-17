from src.system.context import Context


def add_admin(system_admin_id, system_admin_name, system_admin_pass):
    con = Context.db_connection
    # Moet er een system admin of superadmin toegevoegd worden? In dit geval heb ik system admin gedaan.
    c = con.cursor()
    c.execute("INSERT INTO users (id, username, password, role_id) VALUES (?, ?, ?, 2)",
              (system_admin_id, system_admin_name, system_admin_pass))
    con.commit()
    print("System Admin Added")


def update_admin():
    pass


def delete_admin(admin_id):
    con = Context.db_connection
    c = con.cursor()
    c.execute("DELETE FROM users WHERE id = ? AND (role_id = 1 OR role_id = 2)", (admin_id,))
    con.commit()
    print("Admin Deleted")


def reset_admin_password(new_temp_password, admin_id):
    con = Context.db_connection
    c = con.cursor()
    c.execute("UPDATE users SET password = ? WHERE id = ? AND (role_id = 1 OR role_id = 2)",
              (new_temp_password, admin_id))
    con.commit()
    print("Password Updated")
