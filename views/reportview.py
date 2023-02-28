from prettytable import PrettyTable
import os

class ReportView ():
    
    def __init__(self):
        self.table = PrettyTable()
        self.display_report_header_all_players = [
            "player_id",
            "first_name",
            "last_name",
            "date_of_birth",
            "score_of_player",
            "ranking",
        ]   
        self.display_report_header_all_tournaments =[
            "tournament_id",
            "tournament_name",
            "tournament_site",
            "start_date",
            "end_date",
            "number_of_rounds",
            "current_round",
            "general_remarks",
            "participants"

        ]
    
    def report_menu(self):
        options = [
            "get all the players present in the DB in alphabetical order (last name)", 
            "list of all tournaments"
        ]
        menu = "\n".join([f"{i}- {option}" for i, option in enumerate(options, start=1)])
        return print(menu)

    def display_all_players_by_last_name(self, players):
        field_names = self.display_report_header_all_players
        rows = []
        for player in players:
            rows.append([
                player[field_name.lower()] for field_name in field_names
            ])
        self.table.clear()
        self.table.field_names = field_names
        self.table.align = "c"
        self.table.add_rows(rows)
        print("all the players present in the DB in alphabetical order (last name)")
        print(self.table)
    
    def display_all_tournaments_report(self, tournaments):
        """Display tournament reports"""
        self.table.clear()
        self.table.field_names = self.display_report_header_all_tournaments
        self.table.align = "l"

        for i in range(len(tournaments)):
            participants = []
            players = tournaments[i]["players"]
            for k in range(len(players)):
                participants.append(str(players[k]["player_id"]) + " : " + players[k]["last_name"])

            self.table.add_row([
                tournaments[i]["tournament_id"],
                tournaments[i]["tournament_name"],
                tournaments[i]["tournament_site"],
                tournaments[i]["start_date"],
                tournaments[i]["end_date"],
                tournaments[i]["number_of_rounds"],
                tournaments[i]["current_round"],
                tournaments[i]["general_remarks"],
                participants
            ])

        os.system('mode con: cols=200 lines=90')
        print(self.table)
