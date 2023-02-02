from tinydb import TinyDB

class Tournament():

    db_tournament = TinyDB('database/tournaments.json', indent=4)

    def __init__(self,t_id, tournament_name, tournament_site, start_date, end_date, number_of_rounds=4, current_round=1, general_remarks=""):       
        self.t_id = t_id
        self.tournament_name = tournament_name
        self.tournament_site = tournament_site
        self.start_date = str(start_date)
        self.end_date = str(end_date)
        self.number_of_rounds = number_of_rounds
        self.current_round = current_round
        self.general_remarks = general_remarks

    def __str__(self):
            return f"(tournament name : {self.tournament_name}\n tournament ID : {self.t_id})"

    def __repr__(self):
        return f"Tournament({self.tournament_name}, {self.t_id})"

    def format_tournament_data(self):
        return {
            "tournament_name": self.tournament_name,
            "torunament_site": self.tournament_site,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "number_of_rounds": self.number_of_rounds,
            "current_round": self.current_round,
            "general_remarks": self.general_remarks
        }
    
    def save_tournament_in_db(self):
        return self.db_tournament.insert(self.format_tournament_data())
    
    @staticmethod
    def search_tournament_in_db(t_id):
        tournament_db = TinyDB('database/tournaments.json')
        result = tournament_db.search(where("t_id") == t_id)   # Search in the database, the tournament corresponding to the iD provided as input.
        if result:
            return result[0]
        return "no tournament in db"

    @staticmethod
    def update_tournament_data( key, value, t_id):
        # db horizontal?
        tournament_db = TinyDB('database/tournaments.json')
        tournament = Tournament.search_tournament_in_db(t_id)
        # print(tournament)
        if tournament:
            return tournament_db.update({key: value}, where("t_id") == t_id)    
        return "erreur dans les paramètres"

    @staticmethod   # can be called without creating an instance of the class
    def load_all_tournament_in_db():
        tournament_db = TinyDB('database/tournament.json')
        return tournament_db.all()




# from faker import Faker
# fake = Faker(locale="fr_FR")
# scores = [1, 2, 3, 4]
# for _ in range(10):
#     tournament = Tournament(
#         tournament_name = fake.first_name(),
#         tournament_site = fake.address(), 
#         start_date = fake.date_this_century(),
#         end_date = fake.date_this_century(),
#         current_round = fake.random_element(elements=scores))
    # print(tournament.save_tournament_in_db())
    # print(repr(tournament))
    # print(tournament)
    # print(tournament.__str__())
    # print(tournament.__repr__())
    # print(tournament.format_tournament_data())
    # print("-"*10)