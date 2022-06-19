from src.database.connection import get_connection
from src.user_interface.login_menu import LoginMenu
from src.user_interface.super_admin_menu import SuperAdminMenu
from src.system.context import Context
from src.user_interface.util.safe_input import safe_input
from src.system.security.validation import *

from src.system.security.encryption import encrypt_all_files

# encrypt_all_files()

# Context.user_id = 2
# Context.user_name = 'nikola'
# Context.db_connection = get_connection()

# menu = SuperAdminMenu()
# menu.run()

if __name__ == "__main__":
    Context.db_connection = get_connection()
    login = LoginMenu()
    login.run()
