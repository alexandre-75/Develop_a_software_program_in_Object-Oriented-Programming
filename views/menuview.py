
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
    def display_new_tournament():
        print("new tournament")
    
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
    
    @staticmethod
    def tournament_saved():
        print("saved to database ok")
    @staticmethod
    def start_tournament_prompt():
        print("\nStart tournament now ? [yes/no] ")

    @staticmethod
    def select_players(players, player_number):
        print(f"\nSelect player {player_number} :\n")
        for i in range(len(players)):
            print(f"[{players[i]['player_id']}]")
            print(f"{players[i]['last_name']}, {players[i]['first_name']}")
            print(f"{players[i]['ranking']} | {players[i]['date_of_birth']}", )
            print("{players[i]['score_player']}")
        
    @staticmethod
    def player_already_selected():
        print("select other player.")

    @staticmethod
    def review_tournament(info, players):
        print(f"{info[0]}, {info[1]}")
        print(f"site: {info[2]}")
        print(f"Rounds: {info[3]}")
        print(f"general_remarks: {info[4]}")

        for i in players:
            print(f"Player {players.index(i) + 1}:")
            print(f"{i['player_id']}")
            print(f"{i['last_name']}, {i['first_name']}")
            print(f"{i['date_of_birth']}")
        print("Save to database ? [yes/no] ")

print(MainMenu.display_main_menu())