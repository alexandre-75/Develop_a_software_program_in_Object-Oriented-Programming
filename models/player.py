from tinydb import TinyDB, where


class Player():

    def __init__(self, first_name="", last_name="", date_of_birth="", player_id="", score_of_player=0, ranking=1):
        self.first_name = str(first_name)
        self.last_name = str(last_name)
        self.date_of_birth = str(date_of_birth)
        self.player_id = str(player_id)
        self.score_of_player = int(score_of_player)
        self.ranking = int(ranking)
        self.adversary = []
        self.players_database = TinyDB("database/players.json", indent=4)

    def format_player_in_database(self):
        return {"player_id": self.player_id,
                "first_name": self.first_name,
                "last_name": self.last_name,
                "date_of_birth": self.date_of_birth,
                "score_of_player": self.score_of_player,
                "ranking": self.ranking,
                "adversary": self.adversary}

    def save_player_in_database(self):
        return self.players_database.insert(self.format_player_in_database())

    @staticmethod
    def load_all_players_from_database():
        players_database = TinyDB('database/players.json')
        players = list(players_database.all())
        return players

    def update_player_in_database(self, option, new_value):
        setattr(self, option, new_value)
        self.players_database.update({option: new_value}, where('player_id') == self.player_id)
