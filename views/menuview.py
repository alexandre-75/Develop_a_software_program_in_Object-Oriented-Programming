class MainMenu():

    def __init__(self):
        pass

    def print_main_menu_options(self):

        """
        Prints the options available in the main menu.
        """

        print("Welcome to the main menu!")
        print("What would you like to do? Select the desired option by entering its number:")
        print("""
        1. Start a Tournament
        2. Add a new player to the database
        3. Load an old profile and continue registration
        4. Update a player in the database
        5. Load an old tournament
        6. select a type of report
        7. Quit
        """)

    def enter_a_number_to_select_a_main_menu_option(self):

        """
        Asks the user to enter a number corresponding to a main menu option.
        Returns:
            An integer representing the user's choice of main menu option.
        """

        user_choice = input("Select the desired option (1-7): ")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice in [1, 2, 3, 4, 5, 6, 7]:
                return user_choice
        print("Invalid input. Please enter a number between 1 and 7.")

    def enter_a_number_to_select_a_report_option(self):

        """
        Asks the user to enter a number corresponding to a report option.
        Returns:
            An integer representing the user's choice of report option.
        """

        user_choice = input("\n Select the desired option (1-5): ")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice in [1, 2, 3, 4, 5]:
                return user_choice
        print("Invalid input. Please enter a number between 1 and 5.")

    def quit_the_program_now(self):

        """
        Asks the user if they want to quit the program.
        """

        print("do you want to quit the program now? (YES or NO) ")

    def enter_a_id(self):

        """
        Asks the user to enter a desired ID.
        Returns:
            A string representing the user's desired ID.
        """

        user_choice = input("select the desired ID : ")
        return user_choice

    def ergonomics(self):

        """
        Prints a separator to improve readability.
        """

        print("\n---------------------")
