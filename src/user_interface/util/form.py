def prompt_input(prompter):
    """ Keeps prompting until value is not null """
    while True:
        value = prompter()

        if value:
            return value


def single_choice(prompter, choices):
    """ Keeps prompting until user types in one of the options """
    options = list([option[1] for option in choices])
    print(f"Please pick one of the following options: {', '.join(options)}")  # only displays the names, not the ids

    while True:
        value = prompter()

        for index, choice in enumerate(options):
            if choice == value:
                return choices[index]  # returns entire object, including id and name
