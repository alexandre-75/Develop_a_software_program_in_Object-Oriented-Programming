from tinydb import TinyDB

class Tournament():

    db_tournament = TinyDB('database/tournaments.json', indent=4)

    def __init__(self, tournament_name, tournament_site, start_date, end_date, number_of_rounds=4, current_round=1, general_remarks=""):
        
        self.tournament_name = tournament_name
        self.tournament_site = tournament_site
        self.start_date = str(start_date)
        self.end_date = str(end_date)
        self.number_of_rounds = number_of_rounds
        self.current_round = current_round
        self.general_remarks = general_remarks

    def format_tournament_data(self):
        """Return tournament info as a dictionary"""
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
        """Save new tournament to database"""
        return self.db_tournament.insert(self.format_tournament_data())




from faker import Faker
fake = Faker(locale="fr_FR")
scores = [1, 2, 3, 4]
for _ in range(10):
    tournament = Tournament(
        tournament_name = fake.first_name(),
        tournament_site = fake.address(), 
        start_date = fake.date_this_century(),
        end_date = fake.date_this_century(),
        current_round = fake.random_element(elements=scores))
    print(tournament.save_tournament_in_db())