import os
from abc import abstractmethod


class Menu:  # abstract class
    _previous_step = None

    def __init__(self):
        self._options = []
        self._label = []

    @abstractmethod
    def run(self):
        """ Override method, every Menu class must implement this method """
        pass

    def _title(self, title):
        """ Usually executed at the top of a `run` method. Clears the console and the prints a message """
        self._clear()
        print(title)

    def _back(self):
        """ Usually ran after a certain task is completed, takes the user back a step"""
        input("\nPress Enter to go back to the Main Menu.")
        self._previous_step.run()

    def _add_label(self, display):
        if self._options:
            highest_listing = max([number[1] for number in self._options])
            self._label.append((highest_listing, display))
        else:
            self._label.append((1, display))

    def _add_menu_option(self, action, display):
        self._options.append((action, len(self._options) + 1, display))

    def _read_input(self):
        """ Reads input and executes a function that corresponds to that specified input """
        key = int(input())

        for option in self._options:
            if key == option[1]:
                option[0]()

    def _display_options(self):
        """ Displays menu options that the user can choose """
        for option in self._options:

            for separation_text in self._label:
                if separation_text[0] == option[1]:
                    print("\n==== " + separation_text[1] + " ====")

            print(f"[{option[1]}] {option[2]}")

    @staticmethod
    def _clear():
        """ Clears the console """
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def _request_input(input_prompt):
        while True:
            user_input = input(input_prompt)

            if user_input != "":
                return user_input
