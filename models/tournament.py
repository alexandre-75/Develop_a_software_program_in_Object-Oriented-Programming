from tinydb import TinyDB, Query, where

class Tournament():

    tournaments_database = TinyDB('database/tournaments.json', indent=4)

    def __init__(self,tournament_id, tournament_name, tournament_site, start_date, end_date, number_of_rounds=4, current_round=1, general_remarks=""):       
        self.tournament_id = tournament_id
        self.tournament_name = tournament_name
        self.tournament_site = tournament_site
        self.start_date = str(start_date)
        self.end_date = str(end_date)
        self.number_of_rounds = number_of_rounds
        self.current_round = current_round
        self.general_remarks = general_remarks
        self.rounds =[]
        self.players=[]

#---------------------------------------------------------------------------------------------
    def __str__(self):
            return f"(Tournament name: {self.tournament_name}\n ID: {self.tournament_id})"

    def __repr__(self):
        return f"Tournament({self.tournament_name}, {self.tournament_id})"
# -------------------------------------------------------------------------------------------
    def add_player_objet_in_players_list(self, player):
        "Add player object in tournament players list attribut."
        self.players.append(player)
        
    def get_players_list(self):
        return self.players
#---------------------------------------------------------------------------------------------
    def add_round_objet_in_rounds_list(self, round):
        "Add round object in tournament rounds list attribut."
        self.rounds.append(round)

    def add_match(self, player1, player2, score1, score2):
        if self.rounds:
            last_round = self.rounds[-1]
            last_round.add_match(player1, player2, score1, score2)



    # def add_new_round(self):
    #     if len(self.rounds) < self.number_of_rounds:
    #         self.rounds.append(Round(len(self.rounds) + 1))

    def format_tournament_in_database(self):
        return {
            "tournament_id":self.tournament_id,
            "tournament_name":self.tournament_name,
            "tournament_site":self.tournament_site,
            "start_date":self.start_date,
            "end_date":self.end_date,
            "number_of_rounds":self.number_of_rounds,
            "current_round":self.current_round,
            "general_remarks":self.general_remarks
        }
    
    def save_tournament_in_database(self):
        return self.tournaments_database.insert(self.format_tournament_in_database())
    
    @staticmethod   # can be called without creating an instance of the class
    def find_tournament_in_database(tournament_id):
        tournaments_database = TinyDB('database/tournaments.json')
        result = tournaments_database.search(where("tournament_id") == tournament_id)   # Search in the database, the tournament corresponding to the id provided as input.
        if result:
            return result[0]
        return "No tournament found in database"

    @staticmethod
    def update_tournament_in_database(key, value, tournament_id):
        tournaments_database = TinyDB('database/tournaments.json')
        tournament = Tournament.find_tournament_in_database(tournament_id)
        if tournament:
            return tournaments_database.update({key:value}, where("tournament_id") == tournament_id)    
        return "Error in parameters"

    @staticmethod
    def load_all_tournaments_from_database():
        tournaments_database = TinyDB('database/tournaments.json')
        return tournaments_database.all()




from faker import Faker
fake = Faker(locale="fr_FR")
scores = [1, 2, 3, 4]
idt = [20, 30, 40]
for _ in range(10):
    tournament = Tournament(
        tournament_id= fake.random_element(elements=idt),
        tournament_name = fake.first_name(),
        tournament_site = fake.address(), 
        start_date = fake.date_this_century(),
        end_date = fake.date_this_century(),
        current_round = fake.random_element(elements=scores))

    # print(tournament.__str__())
    # print(tournament.__repr__())
    # print(tournament.save_tournament_in_database())
    # print(tournament.find_tournament_in_database(20))
    # print(tournament.load_all_tournaments_from_database())
    # print(tournament.update_tournament_in_database("tournament_name", "pepep", 20))
    # print("-"*10)