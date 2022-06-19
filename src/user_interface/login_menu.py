from .menu import Menu
from src.system.security.login import login, try_login_user, SUCCESSFUL_LOGIN, INCORRECT_LOGIN, LOGIN_ATTEMPTS_EXCEEDED
from .util.form import prompt_input
from .util.safe_input import safe_input


class LoginMenu(Menu):
    def run(self):
        self._title(f"Welcome user, this is the Furnicor Family System")
        login_attempt = 1

        while True:
            username = prompt_input(lambda: safe_input("Please input your Username:"))
            password = prompt_input(lambda: safe_input("Please input your Password:"))

            data = try_login_user(username, password, login_attempt)

            if data[0] == SUCCESSFUL_LOGIN:
                break
            elif data[0] == LOGIN_ATTEMPTS_EXCEEDED:
                return exit("Too many login attempts. Action logged.")
            else:
                print("Incorrect username or password, please try again:")
                login_attempt += 1
                continue

        login(data[1][0], data[1][1], data[1][3])
