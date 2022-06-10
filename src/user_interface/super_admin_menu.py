from .system_admin_menu import SystemAdminMenu


class SuperAdminMenu(SystemAdminMenu):
    def __init__(self):
        super().__init__()
        self._add_menu_option(self.add_admin, "Add New Admin")
        self._add_menu_option(self.update_admin, "Update Existing Admin")
        self._add_menu_option(self.delete_admin, "Delete Admin")
        self._add_menu_option(self.reset_admin_password, "Reset Admin Password")

    def run(self):
        self._title(f"Super Admin Menu")
        self._display_options()
        self._read_input()

    def add_admin(self):
        pass

    def update_admin(self):
        pass

    def delete_admin(self):
        pass

    def reset_admin_password(self):
        pass
