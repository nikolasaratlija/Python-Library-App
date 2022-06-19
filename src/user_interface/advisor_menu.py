from .menu import Menu
from src.system.roles.member import Member
import src.system.roles.advisor_service as advisor_service
from src.user_interface.util.form import *
from .util.safe_input import safe_input
from src.system.security.validation import *
from src.system.repository.cities import get_cities
from src.system.repository.members import get_member
from ..system.security.close_application import close_application


class AdvisorMenu(Menu):
    def __init__(self):
        super().__init__()
        self._add_label("Advisor Options")
        self._add_menu_option(self.close_application, "Close Application")
        self._add_menu_option(self.add_member, "Add New Member")
        self._add_menu_option(self.find_member, "Find Member")
        self._add_menu_option(self.modify_member, "Modify Existing Member")
        self._add_menu_option(self.update_own_password, "Update Your Password")

    def run(self):
        self._title(f"Advisor Menu")
        self._display_options()
        self._read_input()

    def close_application(self):
        close_application()
        exit("Gracefully exited the application")

    def add_member(self):
        first_name = prompt_input(lambda: safe_input("Please enter First Name"))
        last_name = prompt_input(lambda: safe_input("Please enter Last Name"))
        email = prompt_input(lambda: safe_input("Please enter Email", is_email))
        zip_code = prompt_input(lambda: safe_input("Please enter Zip Code", is_zipcode))
        phone = prompt_input(lambda: safe_input("Please enter Phone Number", is_phone_number))

        city_options = get_cities()  # gets all cities
        # displays list of cities and prompts user to pick one
        city = single_choice(lambda: safe_input("Please enter a city name: "), city_options)

        result = advisor_service.add_member(
            Member(
                first_name=first_name,
                last_name=last_name,
                email=email,
                zip_code=zip_code,
                phone=phone,
                city_id=city[0]  # id of city
            ))

        print(result[1])

        self._back()

    def find_member(self):
        fields = \
            {'id', 'first_name', 'last_name', 'email', 'phone', 'street_name', 'house_number', 'zip_code', 'city_name'}

        search_parameters = self._multiple_fields_input(fields)
        result = advisor_service.read_member(search_parameters)

        print(result[1])
        self._back()

    def modify_member(self):
        member_id = prompt_input(lambda: safe_input("Please enter a Member id"))
        member = get_member(member_id)

        if not member:
            print("Member with this id does not exist.")
            return self._back()

        print(f"Member '{member['first_name']} {member['last_name']}#{member_id}' found.")
        print("To keep the attribute unchanged, simply keep the field empty and press 'Enter'")

        first_name = prompt_input(lambda: safe_input("Please enter First Name", default_output=member['first_name']))
        last_name = prompt_input(lambda: safe_input("Please enter Last Name", default_output=member['last_name']))
        email = prompt_input(lambda: safe_input("Please enter Email", is_email, default_output=member['email']))
        zip_code = prompt_input(
            lambda: safe_input("Please enter Zip Code", is_zipcode, default_output=member['zip_code']))
        phone = prompt_input(
            lambda: safe_input("Please enter Phone Number", is_phone_number, default_output=member['phone']))

        city_options = get_cities()  # gets all cities
        # displays list of cities and prompts user to pick one
        city = single_choice(lambda: safe_input("Please enter a city name: ", default_output=member['city_id']),
                             city_options)

        result = advisor_service.modify_member(
            member_id=member_id,
            first_name=first_name,
            last_name=last_name,
            email=email,
            zip_code=zip_code,
            phone=phone,
            city_id=city[0],  # id of city
            street_name="test",
            house_number="test"
        )

        print(result[1])

        self._back()

    def update_own_password(self):
        new_pass_prompt = prompt_input(lambda: safe_input("Please enter Password", is_password))

        result = advisor_service.update_own_password(new_pass_prompt)
        print(result[1])

        self._back()
