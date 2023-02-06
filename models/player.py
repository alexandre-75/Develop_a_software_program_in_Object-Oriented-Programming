from tinydb import TinyDB, Query, where
from datetime import datetime
import string

class Player():
    
    players_database = TinyDB("database/players.json", indent=4)

    def __init__(self, first_name, last_name, date_of_birth, player_id): 
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = str(date_of_birth)
        self.player_id = str(player_id)

    def __str__(self):
            return f"(First name: {self.first_name}\n Last name: {self.last_name}\n ID: {self.player_id})"

    def __repr__(self):
        return f"Player({self.first_name}, {self.last_name}, {self.player_id})"
    
    def format_player_in_database(self):
        return {"player_id":self.player_id,
                "first_name":self.first_name,
                "last_name":self.last_name, 
                "birth_date":self.date_of_birth
        }

    def save_player_in_database(self, validate_data = False):
        if validate_data:
            self.validate_player_data()
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
    
    def validate_player_data(self):
        self.validate_player_first_name_and_last_name()
        self.validate_player_date_of_birth()
        # self.validate_player_id()

    def validate_player_first_name_and_last_name(self):
        special_characters = string.punctuation + string.digits
        if not (self.first_name and self.last_name):
            raise ValueError("first name and last name cannot be empty.")
        for i in self.first_name:
            if i in special_characters:
                raise ValueError(f"not valid : {self.first_name}")
        for i in self.last_name:
            if i in special_characters:
                raise ValueError(f"not valid : {self.last_name}")

    def validate_player_date_of_birth(self):
        try:
            datetime.strptime(self.date_of_birth,'%Y-%m-%d')
        except:
            raise ValueError("Invalid format. Use YYYY-MM-DD")
    
    # def validate_player_id(self):
    #     if len(self.player_id) != 7:
    #         raise ValueError("Player ID must be 7 characters long")
    #     if not self.player_id[:2].isalpha() or not self.player_id[2:].isdigit():
    #         raise ValueError("Player ID must start with two letters followed by five digits")
    #     return True
    

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




