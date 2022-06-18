from src.database.connection import get_connection
from src.user_interface.login_menu import LoginMenu
from src.user_interface.super_admin_menu import SuperAdminMenu
from src.system.context import Context

# Context.user_id = 1
# Context.user_name = 'nikola'
# Context.db_connection = get_connection()
#
# menu = SuperAdminMenu()
# menu.run()

# if __name__ == "__main__":
#     Context.db_connection = get_connection()
#     login = LoginMenu()
#     login.run()

from src.system.security.user_id_generator import *

print(generate_user_id())
