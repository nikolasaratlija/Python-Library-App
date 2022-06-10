from src.database.connection import get_connection
from src.system.context import Context
from src.system.exceptions import LoginError

from src.system.roles.advisor import Advisor
from src.system.roles.roles import Roles
from src.system.roles.super_admin import SuperAdmin
from src.system.roles.system_admin import SystemAdmin

from src.user_interface.advisor_menu import AdvisorMenu
from src.user_interface.super_admin_menu import SuperAdminMenu
from src.user_interface.system_admin_menu import SystemAdminMenu


def try_login_user(username, password):
    con = get_connection()
    c = con.cursor()
    c.execute("SELECT * FROM employees WHERE username=? AND password=?", (username, password))
    return c.fetchone()


def login(role_id):
    """ Opens a menu based on the role id of the logged in employee """

    if role_id is Roles.SUPER_ADMIN.value:
        Context.user = SuperAdmin()
        SuperAdminMenu().run()
    elif role_id is Roles.SYSTEM_ADMIN.value:
        Context.user = SystemAdmin()
        SystemAdminMenu().run()
    elif role_id is Roles.ADVISOR.value:
        Context.user = Advisor()
        AdvisorMenu().run()
    else:
        raise LoginError("Error from 'def _open_menu'. Something possibly went wrong with the role_id.")