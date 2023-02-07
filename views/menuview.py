
class MainMenu():
    
    def input_a_number():
        return int(input("Enter a number : "))
        
    def display_main_menu():
        print("""Main Menu :
             1. Tournament
             2. Player
             3. Find a player""")
        return input_a_number()

    def display_tournament_menu():
        print("""Tournament menu:
                1. Start a Tournament
                2. Find a Tournament from the database
                3. Update a Tournament from the database
                4. return""")
        return input_a_number()

    def display_player_menu():
        print("""Player menu:
                1. Add a new player to the database
                2. Find a player from the database
                3. Update a player from the database
                4. Return""")

        return input_a_number()
