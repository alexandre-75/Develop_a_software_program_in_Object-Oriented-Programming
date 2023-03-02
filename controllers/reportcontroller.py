from views.reportview import ReportView
from views.menuview import MainMenu


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
        user_input = self.menu_view.enter_a_id()
        for t in tournaments:
            if t["tournament_id"] == str(user_input):
                self.report_view.display_name_and_dates(t["tournament_name"], t["start_date"], t["end_date"])

    def list_of_tournament_players(self, tournaments):
        tournaments = sorted(tournaments, key=lambda x: x.get("tournament_id"))
        self.report_view.display_all_tournament(tournaments)
        user_input = self.menu_view.enter_a_id()
        for t in tournaments:
            if t["tournament_id"] == str(user_input):
                a = t["players"]
                players = sorted(a, key=lambda x: x.get("last_name"))
                self.report_view.display_all_players_by_last_name(players)

    def list_all_matches_in_all_rounds(self, tournaments):
        tournaments = sorted(tournaments, key=lambda x: x.get("tournament_id"))
        self.report_view.display_all_tournament(tournaments)
        user_input = self.menu_view.enter_a_id()
        for t in tournaments:
            if t["tournament_id"] == str(user_input):
                self.report_view.display_tournament(t)
                matches = []
                round_num = 1
                for r in t["rounds"]:
                    matches_in_round = r[1::2]
                    for m in matches_in_round:
                        if m not in matches:
                            matches.append(m)
                            self.report_view.display_matches_report(round_num, m)
                    round_num += 1
