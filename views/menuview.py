
class MainMenu():

    def __init__(self):
        pass
    
    @staticmethod
    def exit_the_program():
        print("exit the program ? [yes/no] ")

    @staticmethod
    def input_a_number():
        return int(input("Enter a number : "))

    @staticmethod   
    def display_main_menu():
        display = print("""Menu
                Tournament menu:
                1. Start a Tournament
                2. Add a new player to the database
                3. exit""")
        return display

    # def display_tournament_menu():
    #     print("""Tournament menu:
    #             1. Start a Tournament
    #             2. Find a Tournament from the database
    #             3. Update a Tournament from the database
    #             4. return""")
    #     return input_a_number()

    # def display_player_menu():
    #     print("""Player menu:
    #             1. 
    #             2. Find a player from the database
    #             3. Update a player from the database
    #             4. Return""")

    #     return input_a_number()


# print(MainMenu.display_main_menu())