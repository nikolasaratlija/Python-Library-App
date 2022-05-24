from .system_admin_menu import SystemAdminMenu


class SuperAdminMenu(SystemAdminMenu):
    def __init__(self):
        super().__init__()
        self._add_menu_option(lambda: print("Super Admin Option 1 Executed"), "Super Admin Menu Option 1")
        self._add_menu_option(lambda: print("Super Admin Option 2 Executed"), "Super Admin Menu Option 2")
        self._add_menu_option(lambda: print("Super Admin Option 3 Executed"), "Super Admin Menu Option 3")

    def run(self):
        self._title(f"Super Admin Menu")
        self._display_options()
        self._read_input()
