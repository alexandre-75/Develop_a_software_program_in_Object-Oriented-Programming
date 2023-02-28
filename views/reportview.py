from prettytable import PrettyTable

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
    
    def report_menu(self):
        options = [
            "get all the players present in the DB in alphabetical order (last name)", 
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
