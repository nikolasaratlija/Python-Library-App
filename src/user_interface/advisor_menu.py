from .menu import Menu


class AdvisorMenu(Menu):
    def __init__(self):
        super().__init__()
        self._add_menu_option(lambda: print("Advisor Option 1 Executed"), "Advisor Menu Option 1")
        self._add_menu_option(lambda: print("Advisor Option 2 Executed"), "Advisor Menu Option 2")
        self._add_menu_option(lambda: print("Advisor Option 3 Executed"), "Advisor Menu Option 3")

    def run(self):
        self._title(f"Advisor Menu")
        self._display_options()
        self._read_input()
