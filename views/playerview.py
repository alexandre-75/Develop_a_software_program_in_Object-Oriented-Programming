class PlayerView():

    def __init__(self):
        pass

    @staticmethod
    def display_new_player():
        print("creation a new player")
    
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
    def select_players(players):
        for i in range(len(players)):
            print(f"[{players[i]['player_id']}]")
            print(f"{players[i]['last_name']}, {players[i]['first_name']}")
            print(f"{players[i]['ranking']}, {players[i]['date_of_birth']}")
            print(f"{players[i]['score_player']}")
    
    @staticmethod
    def update_player_info(selected_player, options):
        print(f"Updating {selected_player.last_name}, {selected_player.first_name}")
        for i in range(len(options)):
            print(f"[{i+1}] Update {options[i]}")