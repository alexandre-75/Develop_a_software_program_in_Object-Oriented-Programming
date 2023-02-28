from views.reportview import ReportView
from views.menuview import MainMenu

from models.tournament import Tournament

class ReportController():
    def __init__(self):
        self.report_view = ReportView()
        self.menu_view = MainMenu()


    def all_players_sorted_alphabetically(self, players):
        players = sorted(players, key=lambda x: x.get("last_name"))
        self.report_view.display_all_players_by_last_name(players)
    
    def all_tournaments(self, tournaments):
        self.report_view.display_all_tournaments_report(tournaments)
    
    def name_and_dates_of_a_tournament(self, tournaments):
        tournaments = sorted(tournaments, key=lambda x: x.get("tournament_id"))
        self.report_view.display_all_tournament_by_id(tournaments)
        user_input = self.menu_view.enter_a_id_to_select_a_player()
        for t in tournaments:
            if t["tournament_id"] == int(user_input):
                self.report_view.display_name_and_dates_tournament(t["tournament_name"], t["start_date"], t["end_date"])
               