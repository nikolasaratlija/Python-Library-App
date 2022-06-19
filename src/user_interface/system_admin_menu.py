from .advisor_menu import AdvisorMenu
import src.system.roles.system_admin_service as system_admin_service
from .util.form import prompt_input
from .util.safe_input import safe_input
from src.system.security.validation import *
from ..system.repository.users import get_advisor


class SystemAdminMenu(AdvisorMenu):
    def __init__(self):
        super().__init__()
        self._add_label("System Admin Options")
        self._add_menu_option(self.add_advisor, "Add New Advisor")
        self._add_menu_option(self.update_advisor, "Modify Existing Advisor")
        self._add_menu_option(self.delete_advisor, "Delete Advisor")
        self._add_menu_option(self.reset_advisor_password, "Reset Advisor Password")
        self._add_menu_option(self.read_all_users, "List All Users")
        self._add_menu_option(self.delete_member, "Delete Member")
        self._add_menu_option(self.backup_restore, "Restore System From Backup")
        self._add_menu_option(self.backup_create, "Create Backup")
        self._add_menu_option(self.read_logs, "Read logs")

    def run(self):
        self._title(f"System Admin Menu")
        self._display_options()
        self._read_input()

    def add_advisor(self):
        username = prompt_input(lambda: safe_input("Please enter Username", not_empty))
        password = prompt_input(lambda: safe_input("Please enter Password", is_password))

        result = system_admin_service.add_advisor(username, password)

        print(result[1])
        self._back()

    def update_advisor(self):
        advisor_id = prompt_input(lambda: safe_input("Please enter a Advisor id"))
        advisor = get_advisor(advisor_id)

        if not advisor:
            print("Advisor with this id does not exist.")
            return self._back()

        username = prompt_input(lambda: safe_input("Please enter First Name", default_output=advisor['username']))
        password = prompt_input(lambda: safe_input("Please enter Last Name", default_output=advisor['password']))
        # TODO ROLE

        result = system_admin_service.update_advisor(advisor_id, username, password, 3)

        print(result[1])
        self._back()

    def delete_advisor(self):
        advisor_id = prompt_input(lambda: safe_input("Please enter Member id", is_digit))

        result = system_admin_service.delete_advisor(advisor_id)

        print(result[1])
        self._back()

    def reset_advisor_password(self):
        pass

    def read_all_users(self):
        users = system_admin_service.read_all_users()
        for user in users:
            print('{:<20s} {:<20s}'.format(f"Name: {user[0]},", f"Role: {user[1]}"))

    def delete_member(self):
        member_id = prompt_input(lambda: safe_input("Please enter Member id", is_digit))

        result = system_admin_service.delete_member(member_id)

        print(result[1])
        self._back()

    def backup_restore(self):
        result = system_admin_service.restore_backup()
        print(result[1])
        self._back()

    def backup_create(self):
        result = system_admin_service.create_backup()
        print(result[1])
        self._back()

    def read_logs(self):
        print(system_admin_service.read_logs())
        self._back()
