from tinydb import TinyDB, Query, where
from datetime import datetime


class Player():
    
    players_database = TinyDB("database/players.json", indent=4)

    def __init__(self, first_name, last_name, date_of_birth, player_id, score_player=0, ranking=1): 
        self.first_name = str(first_name)
        self.last_name = str(last_name)
        self.date_of_birth = str(date_of_birth)
        self.player_id = str(player_id)
        self.score_player = int(score_player)
        self.ranking = int(ranking)

    def __str__(self):
            return f"(First name:{self.first_name}\n Last name:{self.last_name})"

    def __repr__(self):
        return f"Player({self.first_name},{self.last_name})"
    
    # -----------------------------------------------------------------------------------------------
    
    def format_player_in_database(self):
        return {"player_id":self.player_id,
                "first_name":self.first_name,
                "last_name":self.last_name, 
                "birth_date":self.date_of_birth,
                "score_player":self.score_player,
                "ranking":self.ranking}

    def save_player_in_database(self,):
        return self.players_database.insert(self.format_player_in_database())

    @staticmethod   # can be called without creating an instance of the class
    def find_player_in_database(player_id):
        players_database = TinyDB('database/players.json')
        result = players_database.search(where("player_id") == player_id)   # Search in the database, the player corresponding to the id provided as input.
        if result:
            return result[0]
        return "No player found in database"

    @staticmethod
    def update_player_in_database(key, value, player_id):
        players_database = TinyDB('database/players.json')
        player = Player.find_player_in_database(player_id)
        if player:
            return players_database.update({key:value}, where("player_id") == player_id)    
        return "error in parameters"

    @staticmethod
    def load_all_players_from_database():
        players_database = TinyDB('database/players.json')
        return players_database.all()
    


from faker import Faker
fake = Faker(locale="fr_FR")
scores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for _ in range(10):
    player = Player(first_name = fake.first_name(), 
                    last_name = fake.last_name(), 
                    date_of_birth = fake.date_of_birth(), 
                    player_id = fake.random_element(elements=scores))

    # print("-" * 10)
    # print(player.__str__())
    # print(player.__repr__())
    # print(player.save_player_in_database(validate_data=True))
    # print(player.find_player_in_database("9"))
    # print(player.update_player_in_database("last_name","bonjour", "9"))
    # print(player.load_all_players_from_database())




