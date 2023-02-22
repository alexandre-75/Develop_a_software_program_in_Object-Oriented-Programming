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

    def select_tournament(self, tournaments_list):
        
        if len(tournaments_list) == 0:
            print("No tournaments found.")
        else:
            print("{:<5} {:<20} {:<20} {:<30} {:<15} {:<15} {:<10}".format(
                "ID", "Name", "Location", "Description", "Start Date", "End Date", "Current Round"
            ))
            for tournament in tournaments_list:
                print("{:<5} {:<20} {:<20} {:<30} {:<15} {:<15} {:<10}".format(
                    tournament['tournament_id'],
                    tournament['tournament_name'],
                    tournament['tournament_site'],
                    tournament['start_date'],
                    tournament['end_date'],
                    tournament['general_remarks'],
                    f"Round {tournament['current_round']}/{tournament['number_of_rounds']}"
                ))
    
    def print_error_load_tournament(self):
        print("an error while loading, enter a valid id")