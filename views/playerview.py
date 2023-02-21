class PlayerView():

    def __init__(self):
        pass
      
    def summary_of_new_player_created(self, info):
        print("---------- summary of new player created ----------")
        print(f"first name : {info['first_name']}")
        print(f"Last name : {info['last_name']}")
        print(f"Date of birth : {info['date_of_birth']}")
        print(f"Player ID : {info['player_id']}")
        print(f"Score of player: {info['score_of_player']}")
        print(f"Rank : {info['ranking']}")
    
    def player_message_is_saved_in_the_database(self):
        print("player information is correctly saved in the tournament database")
    
    def display_available_players(self, players):
        print("id, Last Name, First Name")
        for player in players:
            print(f"{player['player_id']:5} ; {player['last_name']} ; {player['first_name']}")
