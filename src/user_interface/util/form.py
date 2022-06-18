def prompt_input(prompter):
    while True:
        value = prompter()

        if value:
            return value
