from src.system.exceptions import LoginError
from src.system.context import Context
from src.system.roles.roles import Roles
from src.user_interface.advisor_menu import AdvisorMenu
from src.user_interface.super_admin_menu import SuperAdminMenu
from src.user_interface.system_admin_menu import SystemAdminMenu
from src.system.logging.logger import log


def try_login_user(username, password):
    con = Context.db_connection
    c = con.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    return c.fetchone()


def login(user_id, name, role_id):
    """ Opens a menu based on the role id of the logged in employee """
    Context.user_id = user_id
    Context.user_name = name

    log('Login', f'User: {name}#{user_id} has logged into the system')

    if role_id is Roles.SUPER_ADMIN.value:
        SuperAdminMenu().run()
    elif role_id is Roles.SYSTEM_ADMIN.value:
        SystemAdminMenu().run()
    elif role_id is Roles.ADVISOR.value:
        AdvisorMenu().run()
    else:
        raise LoginError("Error from 'def _open_menu'. Something possibly went wrong with the role_id.")
