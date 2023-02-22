from tinydb import TinyDB, Query, where

class Tournament():

    def __init__(self,tournament_id, tournament_name, tournament_site, start_date, end_date, number_of_rounds=4, current_round=1, general_remarks="", players=[], rounds=[]):       
        self.tournament_id = int(tournament_id)
        self.tournament_name = str(tournament_name)
        self.tournament_site = str(tournament_site)
        self.start_date = str(start_date)
        self.end_date = str(end_date)
        self.number_of_rounds = int(number_of_rounds)
        self.current_round = int(current_round)
        self.general_remarks = str(general_remarks)
        self.rounds =[]
        self.players=[]

        self.tournaments_database = TinyDB('database/tournaments.json', indent=4)

    def format_tournament_in_database(self):
        return {
            "tournament_id":self.tournament_id,
            "tournament_name":self.tournament_name,
            "tournament_site":self.tournament_site,
            "start_date":self.start_date,
            "end_date":self.end_date,
            "number_of_rounds":self.number_of_rounds,
            "current_round":self.current_round,
            "general_remarks":self.general_remarks,
            "rounds":self.rounds,
            "players":self.players
        }
    
    def save_tournament_in_database(self):
        return self.tournaments_database.insert(self.format_tournament_in_database())

    def load_all_tournaments_from_database(self):
        tournaments_database = TinyDB('database/tournaments.json')
        return tournaments_database.all()
