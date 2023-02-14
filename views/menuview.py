
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
        return print("""Menu
                
                1. Start a Tournament
                2. Add a new player to the database
                3. exit""")
    
    @staticmethod
    def display_new_player():
        print("new player")
    
    @staticmethod
    def input_prompt_text(option):
        print(f"Enter {option} : ")
    
    @staticmethod
    def review_player(info): 
        print("New player created :")
        print(f"{info[0]}, {info[1]}")
        print(f"Date of birth : {info[2]}")
        print(f"player_id : {info[3]}")
        print(f"score_player:{info[4]}")
        print(f"Rank : {info[5]}")
        print("Save to database ? [yes/no] ")

    @staticmethod
    def player_saved():
        print("saved to database ok")

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


print(MainMenu.display_main_menu())