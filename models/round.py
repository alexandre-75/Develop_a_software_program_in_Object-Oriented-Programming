from tinydb import TinyDB, Query, where
# from utils.date_and_time import get_times
# from models.match import Match

class Round:
    
    def __init__(self, round_name, start_date, end_date="_"):
        self.round_name = str(round_name)
        self.start_date = str(start_date)
        self.end_date = str(end_date)
        self.matches_list = []
    
    def add_match_to_list(self, player_1, player_2):
        player_1_name = f"{player_1['last_name']}, {player_1['first_name']}"
        player_1_rank = player_1['ranking']
        player_2_name = f"{player_2['last_name']}, {player_2['first_name']}"
        player_2_rank = player_2['ranking']
        player_1_score = player_1['score_of_player']
        player_2_score = player_2['score_of_player']
        match = (player_1_name, player_1_rank, player_1_score,
                player_2_name, player_2_rank, player_2_score)
        # print(match)
        # print ("TaTAtATATATATATATATATATATATATATATTATATATATATATTATA")
        self.matches_list.append(match)
        # print(self.matches_list)

    def all_information_round(self):
        return [self.round_name, self.start_date, self.end_date, self.matches_list]

    