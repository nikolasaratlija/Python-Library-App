from .menu import Menu
from src.system.roles.member import Member
import src.system.roles.advisor_service as advisor_service
from src.user_interface.util.form import *
from .util.safe_input import safe_input
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
        # TODO add fields
        first_name = prompt_input(lambda: safe_input("Please enter First Name", is_not_empty_or_whitespace))
        last_name = prompt_input(lambda: safe_input("Please enter Last Name", is_not_empty_or_whitespace))
        # email_prompt = prompt_input(lambda: safe_input("Please enter First Name", is_email))
        # zip_code_prompt = prompt_input(lambda: safe_input("Please enter Zip Code", is_zipcode))

        advisor_service.add_member(Member(first_name, last_name))

        self._back()

    def find_member(self):
        fields = \
            {'id', 'first_name', 'last_name', 'email', 'phone', 'street_name', 'house_number', 'zip_code', 'city_name'}

        search_parameters = self._multiple_fields_input(fields)
        result = advisor_service.read_member(search_parameters)

        print(result[1])
        self._back()

    def modify_member(self):
        pass

    def update_own_password(self):
        new_pass_prompt = Prompt("password")  # TODO VALIDATION
        form = Form()
        form.add_prompt(new_pass_prompt)
        form.prompt_form()

        result = advisor_service.update_own_password(new_pass_prompt.get_value())
        print(result[1])

        self._back()
