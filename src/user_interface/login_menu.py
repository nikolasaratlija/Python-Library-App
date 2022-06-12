from .menu import Menu
from src.system.security.login import login, try_login_user
from src.user_interface.util.form import *


class LoginMenu(Menu):
    def run(self):
        self._title(f"Welcome user, this is the Furnicor Family System")
        username_prompt = Prompt("Username")
        password_prompt = Prompt("Password")

        login_form = Form()
        login_form.add_prompt(username_prompt)
        login_form.add_prompt(password_prompt)

        while True:
            login_form.prompt_form()

            data = try_login_user(
                username_prompt.get_value(),
                password_prompt.get_value())

            if not data:
                print("Incorrect username or password, please try again:")
                continue
            else:
                break

        login(data[3])
