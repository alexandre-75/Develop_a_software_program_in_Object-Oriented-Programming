from tinydb import TinyDB, Query, where
# from utils.date_and_time import get_times
# from models.match import Match

class Round:
    
    def __init__(self, round_name, start_date, end_date="_"):
        self.round_name = str(round_name)
        self.start_date = str(start_date)
        self.end_date = str(end_date)
        self.matches_list = []
        self.rounds_database = TinyDB("database/rounds.json", indent=4)