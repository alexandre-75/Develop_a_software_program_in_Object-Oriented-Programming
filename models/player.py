import string
from datetime import datetime
from tinydb import TinyDB

class Player():
    
    db_player = TinyDB("database/players.json", indent=4)
    # L'avantage de définir db_player dans la classe est que vous pouvez utiliser une seule instance de TinyDB pour toutes les instances de la classe
    # The advantage of defining db_player in the class is that you can use a single instance of TinyDB for all instances of the class

    def __init__(self, first_name, surname, date_of_birth):
        self.first_name = first_name
        self.surname = surname
        self.date_of_birth = str(date_of_birth)
    
    def __repr__(self):
        return f"Player({self.first_name}, {self.surname}, {self.date_of_birth})"

    def __str__(self):
        return f"(first name : {self.first_name}\n surname : {self.surname}\n date of birth : {self.date_of_birth})"

    def save_player_in_db(self, validate_data = False):
        if validate_data:
            self.checks()
        return Player.db_player.insert({"first_name":self.first_name, "surname":self.surname, "birth":self.date_of_birth})
    
    @staticmethod   # can be called without creating an instance of the class
    def load_all_player_in_db():
        players_db = TinyDB('database/players.json')
        return players_db.all()

    def checks(self):
        self._check_first_name_and_surname()
        self._check_date_of_birth()

    def _check_first_name_and_surname(self):
        special_characters = string.punctuation + string.digits
        if not (self.first_name and self.surname):
            raise ValueError("first name and last name cannot be empty.")
        for i in self.first_name:
            if i in special_characters:
                raise ValueError(f"not valid : {self.first_name}")
        for i in self.surname:
            if i in special_characters:
                raise ValueError(f"not valid : {self.surname}")

    def _check_date_of_birth(self):
        try:
            datetime.strptime(self.date_of_birth,'%Y-%m-%d')
        except:
            raise ValueError("Invalid format. Use YYYY-MM-DD")
    

from faker import Faker
fake = Faker(locale="fr_FR")
for _ in range(10):
    player = Player(first_name = fake.first_name(), surname = fake.last_name(), date_of_birth = fake.date_of_birth())
    # player._check_first_name_and_surname()
    # player._check_date_of_birth()
    # print(repr(player))
    # print("-" * 10)
    # print(string.punctuation)
    # print(player.save_player_in_db(validate_data = True))
    print(player.load_player_db())

