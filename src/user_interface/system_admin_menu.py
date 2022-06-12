from .advisor_menu import AdvisorMenu
import src.system.roles.system_admin_service as system_admin_service


class SystemAdminMenu(AdvisorMenu):
    def __init__(self):
        super().__init__()
        self._add_label("System Admin Options")
        self._add_menu_option(self.add_advisor, "Add New Advisor")
        self._add_menu_option(self.modify_advisor, "Modify Existing Advisor")
        self._add_menu_option(self.delete_advisor, "Delete Advisor")
        self._add_menu_option(self.reset_advisor_password, "Reset Advisor Password")
        self._add_menu_option(self.read_all_users, "List All Users")
        self._add_menu_option(self.delete_member, "Delete Member")
        self._add_menu_option(self.backup, "Back-Up System")
        self._add_menu_option(self.read_logs, "Read logs")

    def run(self):
        self._title(f"System Admin Menu")
        self._display_options()
        self._read_input()

    def add_advisor(self):
        pass

    def modify_advisor(self):
        pass

    def delete_advisor(self):
        pass

    def reset_advisor_password(self):
        pass

    def read_all_users(self):
        users = system_admin_service.read_all_users()
        for user in users:
            print('{:<20s} {:<20s}'.format(f"Name: {user[0]},", f"Role: {user[1]}"))

    def delete_member(self):
        pass

    def backup(self):
        pass

    def read_logs(self):
        pass
