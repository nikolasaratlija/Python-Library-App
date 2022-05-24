from menu import Menu
from advisor_menu import AdvisorMenu
from super_admin_menu import SuperAdminMenu
from system_admin_menu import SystemAdminMenu


class MainMenu(Menu):
    def __init__(self):
        super().__init__()

        advisor_menu = AdvisorMenu()
        system_admin_menu = SystemAdminMenu()
        super_admin_menu = SuperAdminMenu()

        self._add_menu_option(lambda: advisor_menu.run(), "Open Advisor Menu")
        self._add_menu_option(lambda: system_admin_menu.run(), "Open System Admin Menu")
        self._add_menu_option(lambda: super_admin_menu.run(), "Super Admin Menu")

    def run(self):
        self._title(f"Welcome user, this is the Furnicor Family System\n"
                    f"To open a menu, type a number and then press 'Enter'")
        self._display_options()
        self._read_input()
