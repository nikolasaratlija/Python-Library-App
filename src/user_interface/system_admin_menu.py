from .advisor_menu import AdvisorMenu


class SystemAdminMenu(AdvisorMenu):
    def __init__(self):
        super().__init__()
        self._add_menu_option(lambda: print("System Admin Option 1 Executed"), "System Admin Menu Option 1")
        self._add_menu_option(lambda: print("System Admin Option 2 Executed"), "System Admin Menu Option 2")
        self._add_menu_option(lambda: print("System Admin Option 3 Executed"), "System Admin Menu Option 3")

    def run(self):
        self._title(f"System Admin Menu")
        self._display_options()
        self._read_input()
