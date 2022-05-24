from .menu import Menu
from .advisor_menu import AdvisorMenu
from .super_admin_menu import SuperAdminMenu
from .system_admin_menu import SystemAdminMenu

from src.system.roles.roles import Roles
from src.database.connection import get_connection
from src.system.exceptions import LoginError


def _try_login_user(username, password):
    con = get_connection()
    c = con.cursor()
    c.execute("SELECT * FROM employees WHERE username=? AND password=?", (username, password))
    return c.fetchone()


class LoginMenu(Menu):
    def run(self):
        self._title(f"Welcome user, this is the Furnicor Family System")

        while True:
            username = self._request_input("Please enter your username:")
            password = self._request_input("Please enter your password:")

            data = _try_login_user(username, password)

            if not data:
                print("Incorrect username or password, please try again:")
                continue
            else:
                break

        _open_menu(data[3])


def _open_menu(role_id):
    """ Opens a menu based on the role id of the logged in employee """

    if role_id is Roles.SUPER_ADMIN.value:
        SuperAdminMenu().run()
    elif role_id is Roles.SYSTEM_ADMIN.value:
        SystemAdminMenu().run()
    elif role_id is Roles.ADVISOR.value:
        AdvisorMenu().run()
    else:
        raise LoginError("Error from 'def _open_menu'. Something possibly went wrong with the role_id.")
