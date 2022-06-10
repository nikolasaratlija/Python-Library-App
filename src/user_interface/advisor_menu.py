from .menu import Menu
from src.system.roles.advisor import Advisor
from src.system.roles.advisor import Member
from src.system.context import Context


class AdvisorMenu(Menu):
    def __init__(self):
        super().__init__()
        self._add_menu_option(self.add_member, "Add New Member")
        self._add_menu_option(self.find_member, "Find Member")
        self._add_menu_option(self.modify_member, "Modify Existing Member")
        self._add_menu_option(self.update_own_password, "Update Your Password")

    def run(self):
        self._title(f"Advisor Menu")
        self._display_options()
        self._read_input()

    def add_member(self):
        Context.user.add_member(
            Member("Nikola",
                   "Saratlija")
        )

    def find_member(self):
        pass

    def modify_member(self):
        pass

    def update_own_password(self):
        pass
