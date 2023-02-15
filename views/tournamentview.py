
class TournamentView():
    def __init__(self):
        pass

    @staticmethod
    def display_new_tournament():
        print(" creation a new tournament")
    
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
    
    @staticmethod
    def tournament_saved():
        print("saved to database ok")

    @staticmethod
    def start_tournament_prompt():
        print("\nStart tournament now ? [yes/no] ")
    
    @staticmethod
    def select_tournament(tournaments):
        for tournament in tournaments:
            print(f"{tournament['tournament_id']}, {tournament['tournament_name']}, {tournament['tournament_site']}, {tournament['general_remarks']} "
                f"Started on : {tournament['start_date']} | Ended on : {tournament['end_date']} | "
                f"Round {tournament['current_round']},{tournament['number_of_rounds']}, players:[{tournament[player]}]")
            print("[back] Back to main menu")