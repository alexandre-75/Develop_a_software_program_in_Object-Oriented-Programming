class MainMenu():

    def __init__(self):
        pass
    
    def print_main_menu_options(self):
        print("Welcome to the main menu!")
        print("What would you like to do? Select the desired option by entering its number:")
        print(""" 
        1. Start a Tournament
        2. Add a new player to the database
        3. Update a player in the database
        4. Load an old tournament
        5. select a type of report
        6. Quit
        """)
            
    def enter_a_number_to_select_a_main_menu_option(self):
        
        """Ask the user to select a main menu option by entering a number between 1 and 6.
        Returns:
        - An integer value corresponding to the selected option.
        Raises:
        - ValueError if the input is not a valid integer between 1 and 6."""
        
        user_choice = input("Select the desired option (1-6): ")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice in [1, 2, 3, 4, 5, 6]:
                return user_choice
        print("Invalid input. Please enter a number between 1 and 6.")

    def enter_a_number_to_select_a_report_option(self):          
        user_choice = input("Select the desired option (1-#): ")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice in [1, 2]:
                return user_choice
        print("Invalid input. Please enter a number between 1 and #.")
    
    def quit_the_program_now(self):
        print("do you want to quit the program now? (YES or NO) ")