from src.user_interface.login_menu import LoginMenu
from src.user_interface.super_admin_menu import SuperAdminMenu

import src.system.roles.advisor_service as advisor_service

print(advisor_service.read_member(1))

# menu = SuperAdminMenu()
# menu.run()

# if __name__ == "__main__":
#     login = LoginMenu()
#     login.run()
