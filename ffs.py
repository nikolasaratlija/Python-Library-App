from src.database.connection import get_connection
from src.system.security.close_application import close_application
from src.system.security.encryption import encrypt_all_files, decrypt_all_files
from src.user_interface.login_menu import LoginMenu
from src.user_interface.super_admin_menu import SuperAdminMenu
from src.system.context import Context
from src.user_interface.util.safe_input import safe_input
from src.system.security.validation import *

# decrypt_all_files()
Context.user_id = 2
Context.user_name = 'nikola'
decrypt_all_files()
Context.db_connection = get_connection()
#
menu = SuperAdminMenu()
menu.run()

# close_application()

# if __name__ == "__main__":
#     Context.db_connection = get_connection()
#     login = LoginMenu()
#     login.run()
