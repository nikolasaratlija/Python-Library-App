from src.database.connection import get_connection
from src.user_interface.login_menu import LoginMenu
from src.system.context import Context
from src.system.security.encryption import decrypt_all_files

if __name__ == "__main__":
    decrypt_all_files()
    Context.db_connection = get_connection()
    login = LoginMenu()
    login.run()
