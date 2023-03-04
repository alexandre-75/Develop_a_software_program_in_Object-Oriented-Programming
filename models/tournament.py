from tinydb import TinyDB, where


class Tournament():

    def __init__(self, tournament_id="", tournament_name="", tournament_site="",
                 start_date="", end_date="", number_of_rounds=4, current_round=1,
                 general_remarks="", players=[], rounds=[]):
        self.tournament_id = str(tournament_id)
        self.tournament_name = str(tournament_name)
        self.tournament_site = str(tournament_site)
        self.start_date = str(start_date)
        self.end_date = str(end_date)
        self.number_of_rounds = int(number_of_rounds)
        self.current_round = int(current_round)
        self.general_remarks = str(general_remarks)
        self.rounds = []
        self.players = []

        self.tournaments_database = TinyDB('database/tournaments.json', indent=4)

    def format_tournament_in_database(self):
        return {
            "tournament_id": self.tournament_id,
            "tournament_name": self.tournament_name,
            "tournament_site": self.tournament_site,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "number_of_rounds": self.number_of_rounds,
            "current_round": self.current_round,
            "general_remarks": self.general_remarks,
            "rounds": self.rounds,
            "players": self.players
        }

    def deserialize_tournament(self, serialized_tournament):
        self.tournament_id = serialized_tournament['tournament_id']
        self.tournament_name = serialized_tournament['tournament_name']
        self.tournament_site = serialized_tournament['tournament_site']
        self.start_date = serialized_tournament['start_date']
        self.end_date = serialized_tournament['end_date']
        self.number_of_rounds = serialized_tournament['number_of_rounds']
        self.current_round = serialized_tournament['current_round']
        self.general_remarks = serialized_tournament['general_remarks']
        self.rounds = serialized_tournament['rounds']
        self.players = serialized_tournament['players']
        return self

    def save_tournament_in_database(self):
        return self.tournaments_database.insert(self.format_tournament_in_database())

    def load_all_tournaments_from_database(self):
        tournaments_database = TinyDB('database/tournaments.json')
        return tournaments_database.all()

    def update_timer(self, value, key, tournament_id):
        database = self.tournaments_database
        database.update({key: value}, where("tournament_id") == tournament_id)

    def sort_players_by_rank(self):
        return self.players.sort(key=lambda player: player['rank'])

    def sort_players_by_score(self):
        self.players.sort(key=lambda player: player['score_of_player'])
        return self.players

    def split_players(self, a):
        half = len(a) // 2
        top_half = a[:half]
        bottom_half = a[half:]
        return top_half, bottom_half

    def update_tournament_from_database(self):
        db = self.tournaments_database
        db.update({'rounds': self.rounds}, where('tournament_id') == self.tournament_id)
        db.update({'players': self.players}, where('tournament_id') == self.tournament_id)
        db.update({'current_round': self.current_round}, where('tournament_id') == self.tournament_id)
