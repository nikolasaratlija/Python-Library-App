from .system_admin_menu import SystemAdminMenu
import src.system.roles.super_admin_service as super_admin_service
from .util.form import prompt_input
from .util.safe_input import safe_input
from src.system.security.validation import *
from ..system.repository.users import get_admin


class SuperAdminMenu(SystemAdminMenu):
    def __init__(self):
        super().__init__()
        self._add_label("Super Admin Options")
        self._add_menu_option(self.add_admin, "Add New Admin")
        self._add_menu_option(self.update_admin, "Update Existing Admin")
        self._add_menu_option(self.delete_admin, "Delete Admin")
        self._add_menu_option(self.reset_admin_password, "Reset Admin Password")

    def run(self):
        self._title(f"Super Admin Menu")
        self._display_options()
        self._read_input()

    def add_admin(self):
        username = prompt_input(lambda: safe_input("Please enter Username", not_empty))
        password = prompt_input(lambda: safe_input("Please enter Password", is_password))

        result = super_admin_service.add_admin(username, password)
        print(result[1])

        self._back()

    def update_admin(self):
        admin_id = prompt_input(lambda: safe_input("Please enter a Admin id"))
        admin = get_admin(admin_id)

        if not admin:
            print("Admin with this id does not exist.")
            return self._back()

        username = prompt_input(lambda: safe_input("Please enter First Name", default_output=admin['username']))
        password = prompt_input(lambda: safe_input("Please enter Last Name", default_output=admin['password']))
        # TODO ROLE

        result = super_admin_service.update_admin(admin_id, username, password, 2)

        print(result[1])
        self._back()

    def delete_admin(self):
        admin_id = prompt_input(lambda: safe_input("Please enter Admin ID", is_digit))

        result = super_admin_service.delete_admin(admin_id)

        print(result[1])
        self._back()

    def reset_admin_password(self):
        pass
