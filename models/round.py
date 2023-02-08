from tinydb import TinyDB, Query, where
from utils.date_and_time import get_times
# from models.match import Match

class Round:

    rounds_database = TinyDB("database/rounds.json", indent=4)

    def __init__(self, round_name,):
        self.round_name = round_name
        self.start_date = ""
        self.round_open = False
        self.end_date = ""
        self.round_closed = False
        self.matches_list = []

 #---------------------------------------------------------------------------------------
 
    def __str__(self):
        return f"Round name:{self.round_name} "
    
    def __repr__(self):
        return f"Round({self.round_name})"

 #---------------------------------------------------------------------------------------

    def close_round(self):
        self.end_date = get_times()
        self.round_closed = True
        return self.horodatage_end

    @property
    def closed(self):
        return self.round_closed

    def round_open(self):
        self.start_date = get_times()
        self.round_open = True
        return self.start_date

    @property
    def open(self):
        return self.round_open

 #--------------------------------------------------------------------------------------- 

    def add_match_in_round(self, player_1, score_p1, player_2, score_p2):
        self.matches.append(Match(player_1, score_p1, player_2, score_p2))
    
    @property
    def len_matches_list(self):
        return len(self.matches)

 #--------------------------------------------------------------------------------------

    def format_round_in_database(self):
        return {
                "round_name":self.round_name,
                "start_date":self.start_date,
                "end_start": self.end_date,
        }

    def save_round_in_database(self):
            return self.rounds_database.insert(self.format_round_in_database())

 #---------------------------------------------------------------------------------------
    
    @staticmethod   # can be called without creating an instance of the class
    def find_round_in_database(round_name):
        rounds_database = TinyDB('database/rounds.json')
        result = rounds_database.search(where("round_name") == round_name)   # Search in the database, the round corresponding to the id provided as input.
        if result:
            return result[0]
        return "No round found in database"

    @staticmethod
    def update_round_in_database(key, value, round_name):
        rounds_database = TinyDB('database/rounds.json')
        round = Round.find_round_in_database(round_name)
        if round:
            return rounds_database.update({key:value}, where("round_name") == round_name)    
        return "error in parameters"

    @staticmethod
    def load_all_rounds_from_database():
        rounds_database = TinyDB('database/rounds.json')
        return rounds_database.all()
#------------------------------------------------------------------------------

from faker import Faker
fake = Faker(locale="fr_FR")
test_r_id= [0, 1, 2, 3, 4]
for _ in range(10):
    round = Round(
        round_name = fake.first_name(),
        start_date= fake.date_of_birth(),
        end_date = fake.date_of_birth())
   
    # print(round.__str__())
    # print(round.__repr__())
    # print(round.save_round_in_database())
    # print(round.find_round_in_database("1"))
    # print(round.load_all_rounds_from_database())
    # print(round.update_round_in_database("round_name", "alex", 4))
    # print("_"*10)