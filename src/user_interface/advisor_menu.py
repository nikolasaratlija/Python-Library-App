from .menu import Menu
from src.system.roles.advisor import Member
from src.system.context import Context
from src.user_interface.util.form import *
from src.system.security.validation import *


class AdvisorMenu(Menu):
    def __init__(self):
        super().__init__()
        self._add_label("Advisor Options")
        self._add_menu_option(self.add_member, "Add New Member")
        self._add_menu_option(self.find_member, "Find Member")
        self._add_menu_option(self.modify_member, "Modify Existing Member")
        self._add_menu_option(self.update_own_password, "Update Your Password")

    def run(self):
        self._title(f"Advisor Menu")
        self._display_options()
        self._read_input()

    def add_member(self):
        first_name_prompt = Prompt("First Name")
        last_name_prompt = Prompt("Last Name")
        email_prompt = Prompt("Email", EMAIL)
        zip_code_prompt = Prompt("Zip Code", ZIPCODE)

        form = Form()
        form.add_prompt(first_name_prompt)
        form.add_prompt(last_name_prompt)
        form.add_prompt(email_prompt)
        form.add_prompt(zip_code_prompt)

        form.prompt_form()

        Context.user.add_member(
            Member(first_name_prompt.get_value(), last_name_prompt.get_value()))

    def find_member(self):
        pass

    def modify_member(self):
        pass

    def update_own_password(self):
        pass
