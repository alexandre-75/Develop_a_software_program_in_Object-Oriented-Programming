from tinydb import TinyDB, Query, where


class Match():

    matches_database = TinyDB("database/matches.json", indent=4)
  
    def __init__(self, match_id, player_1, score_p1, player_2, score_p2):
        self.match_id = str(match_id)
        self.match = ([player_1, score_p1], [player_2, score_p2])   # single match stored as a tuple containing two lists
