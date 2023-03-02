class Match():

    def __init__(self, match_id, player_1, score_p1, player_2, score_p2):
        self.match_id = str(match_id)
        self.match = ([player_1, score_p1], [player_2, score_p2])
