class TournamentView():

    def __init__(self):
        pass
    
    def summary_of_new_tournament_created(self, info, players):
            print(f"{info['tournament_id']}, {info['tournament_name']}")
            print(f"site: {info['tournament_site']}")
            print(f"Rounds: {info['current_round']}/{info['number_of_rounds']}")
            print(f"general_remarks: {info['general_remarks']}")

            for i in players:
                print(f"Player {players.index(i) + 1}:")
                print(f"{i['player_id']}")
                print(f"{i['last_name']}, {i['first_name']}")
                print(f"{i['date_of_birth']}")

    def tournament_message_is_saved_in_the_database(self):
        print("tournament information is correctly saved")

    def message_start_tournament(self):
        print("Start tournament now ? [yes/no] ")

    def invalid_player_id(self):
        print("the identifier is not recognized, try again")
