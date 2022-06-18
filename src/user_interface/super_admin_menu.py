from .system_admin_menu import SystemAdminMenu
import src.system.roles.super_admin_service as super_admin_service
from .util.form import Prompt, Form


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
        username = Prompt("username")  # TODO INPUT VALIDATION
        password = Prompt("password")  # TODO INPUT VALIDATION

        form = Form()
        form.add_prompt(username)
        form.add_prompt(password)

        form.prompt_form()

        result = super_admin_service.add_admin(username.get_value(), password.get_value())
        print(result[1])

        self._back()

    def update_admin(self):
        pass

    def delete_admin(self):
        admin_id = Prompt("admin_id")  # TODO INPUT VALIDATION

        form = Form()
        form.add_prompt(admin_id)

        form.prompt_form()

        result = super_admin_service.delete_admin(admin_id.get_value())

        print(result[1])

        self._back()

    def reset_admin_password(self):
        pass
