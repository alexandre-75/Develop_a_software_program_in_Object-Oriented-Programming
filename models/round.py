class Round:
    
    def __init__(self, round_name):
        self.round_name = str(round_name)
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
        self.matches_list.append(match)

    def all_information_round(self):
        return [self.round_name, self.matches_list]

    