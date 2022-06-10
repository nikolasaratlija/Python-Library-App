from .menu import Menu
from src.system.security.login import login, try_login_user


class LoginMenu(Menu):
    def run(self):
        self._title(f"Welcome user, this is the Furnicor Family System")

        while True:
            username = self._request_input("Please enter your username:")
            password = self._request_input("Please enter your password:")

            data = try_login_user(username, password)

            if not data:
                print("Incorrect username or password, please try again:")
                continue
            else:
                break

        login(data[3])
