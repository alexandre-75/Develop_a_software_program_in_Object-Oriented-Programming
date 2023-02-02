from tinydb import TinyDB
from models.match import Match

class Round:

    db_round = TinyDB("database/rounds.json", indent=4)

    def __init__(self, r_id, round_name, beginning_date, ending_date):
        self.r_id = r_id
        self.round_name = round_name
        self.beginning_date = beginning_date
        self.ending_date = ending_date
        self.match_list = []
    
    def __str__(self):
        return f"round name:{self.round_name}\n round ID: {self.r_id}"
    
    def __repr__(self):
        return f"Round({self.round_name}, {self.r_id})"
    
    def format_round_data(self):
        return {"round_ID": self.r_id,
                "round_name":self.round_name,
                "start date":self.beginning_date,
                "end start": self.ending_date,}

    def save_round_in_db(self):
            return self.db_round.insert(self.format_round_data())
    
    @staticmethod
    def search_round_in_db(m_id):
        round_db = TinyDB('database/rounds.json')
        result = round_db.search(where("r_id") == r_id)   # Search in the database, the round corresponding to the iD provided as input.
        if result:
            return result[0]
        return "no round in db"

    @staticmethod
    def update_round_data( key, value, r_id):
        # db horizontal?
        round_db = TinyDB('database/rounds.json')
        round = Round.search_round_in_db(p_id)
        # print(round)
        if round:
            return round_db.update({key: value}, where("r_id") == r_id)    
        return "erreur dans les paramètres"

    @staticmethod   # can be called without creating an instance of the class
    def load_all_round_in_db():
        round_db = TinyDB('database/round.json')
        return round_db.all()



    # def add_match(self, match):
    #     self.match_list.append(match)

    