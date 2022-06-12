from src.database.connection import get_connection
from src.system.exceptions import LoginError

from src.system.roles.roles import Roles

from src.user_interface.advisor_menu import AdvisorMenu
from src.user_interface.super_admin_menu import SuperAdminMenu
from src.user_interface.system_admin_menu import SystemAdminMenu


def try_login_user(username, password):
    con = get_connection()
    c = con.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    return c.fetchone()


def login(role_id):
    """ Opens a menu based on the role id of the logged in employee """

    if role_id is Roles.SUPER_ADMIN.value:
        SuperAdminMenu().run()
    elif role_id is Roles.SYSTEM_ADMIN.value:
        SystemAdminMenu().run()
    elif role_id is Roles.ADVISOR.value:
        AdvisorMenu().run()
    else:
        raise LoginError("Error from 'def _open_menu'. Something possibly went wrong with the role_id.")
