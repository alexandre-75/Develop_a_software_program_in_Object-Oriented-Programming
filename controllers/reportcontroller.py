from views.reportview import ReportView
from models.tournament import Tournament

class ReportController():
    def __init__(self):
        self.report_view = ReportView()

    def all_players_sorted_alphabetically(self, players):
        players = players = sorted(players, key=lambda x: x.get('last_name'))
        self.report_view.display_all_players_by_last_name(players)
    
    def all_tournaments(self, tournaments):
        self.report_view.display_all_tournaments_report(tournaments)