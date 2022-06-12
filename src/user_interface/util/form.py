from src.system.security.validation import Validation, validate_input


class Prompt:
    def __init__(self, label, validation: Validation = None):
        self.label = label
        self.validation = validation
        self._value = None

    def prompt_input(self):
        while True:
            value = input(f"Please enter a value for '{self.label}':")

            if not validate_input(value, self.validation):
                print(self.validation.error_message)
            else:
                self._value = value
                break

    def get_value(self):
        return self._value


class Form:
    def __init__(self):
        self.prompts = []

    def add_prompt(self, prompt: Prompt):
        self.prompts.append(prompt)

    def prompt_form(self):
        for prompt in self.prompts:
            prompt.prompt_input()
