from tinydb import TinyDB, Query, where
# from models.match import Match

class Round:

    rounds_database = TinyDB("database/rounds.json", indent=4)

    def __init__(self, round_id, round_name, start_date, end_date):
        self.round_id = str(round_id)
        self.round_name = round_name
        self.start_date = str(start_date)
        self.end_date = str(end_date)
        # self.match_list = []
    
    def __str__(self):
        return f"Round name:{self.round_name}\n ID: {self.round_id}"
    
    def __repr__(self):
        return f"Round({self.round_name}, {self.round_id})"
    
    def format_round_in_database(self):
        return {"round_id": self.round_id,
                "round_name":self.round_name,
                "start_date":self.start_date,
                "end_start": self.end_date,
        }

    def save_round_in_database(self):
            return self.rounds_database.insert(self.format_round_in_database())
    
    @staticmethod   # can be called without creating an instance of the class
    def find_round_in_database(round_id):
        rounds_database = TinyDB('database/rounds.json')
        result = rounds_database.search(where("round_id") == round_id)   # Search in the database, the round corresponding to the id provided as input.
        if result:
            return result[0]
        return "No round found in database"

    @staticmethod
    def update_round_in_database(key, value, round_id):
        rounds_database = TinyDB('database/rounds.json')
        round = Round.find_round_in_database(round_id)
        if round:
            return rounds_database.update({key:value}, where("round_id") == round_id)    
        return "error in parameters"

    @staticmethod
    def load_all_rounds_from_database():
        rounds_database = TinyDB('database/rounds.json')
        return rounds_database.all()

    # def add_match(self, match):
    #     self.match_list.append(match)

    

from faker import Faker
fake = Faker(locale="fr_FR")
test_r_id= [0, 1, 2, 3, 4]
for _ in range(10):
    round = Round(
        round_id= fake.random_element(elements=test_r_id),
        round_name = fake.first_name(),
        start_date= fake.date_of_birth(),
        end_date = fake.date_of_birth())
   
    # print(round.__str__())
    # print(round.__repr__())
    # print(round.save_round_in_database())
    # print(round.find_round_in_database("1"))
    # print(round.load_all_rounds_from_database())
    # print(round.update_round_in_database("round_name", "alex", 4))
    print("_"*10)