from prettytable import PrettyTable


class ReportView():

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
        self.display_report_header_all_tournaments = [
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
        self.display_header_tournament_id = ["tournament_id"]
        self.display_header_tournament = [
            "tournament_id",
            "tournament_name",
            "tournament_site",
            "start_date",
            "end_date",
        ]
        self.matches_report_field_names = [
                "Name P1",
                "Rank P1",
                "Score P1",
                " ",
                "Name P2",
                "Rank P2",
                "Score P2"
            ]

    def report_menu(self):

        """
        Displays a menu with a list of options for generating different reports.
        Returns:
            None
        """

        options = [
            "get all the players present in the DB in alphabetical order (last name)",
            "list of all tournaments",
            "name and dates of a tournament",
            "list of tournament players in alphabetical order",
            "list all matches in all rounds of a tournament"
        ]
        menu = "\n".join([f"{i}- {option}" for i, option in enumerate(options, start=1)])
        return print(menu)

    def display_all_players_by_last_name(self, players):

        """
        Displays a table of all players sorted by last name.
        Args:
            players (list): A list of player dictionaries.
        Returns:
            None
        """

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
        print("all the players present (last name)")
        print(self.table)

    def display_all_tournaments_report(self, tournaments):

        """
        Displays a table of all tournaments with information on participants.
        Args:
            tournaments (list): A list of tournament dictionaries.
        Returns:
            None
        """

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
        print(self.table)

    def display_all_tournament_by_id(self, tournaments):

        """
        Displays a table of all tournaments sorted by tournament ID.
        Args:
            tournaments (list): A list of tournament dictionaries.
        Returns:
            None
        """

        field_id = self.display_header_tournament_id
        rows = []
        for tournament in tournaments:
            rows.append([
                tournament[field.lower()] for field in field_id
            ])
        self.table.clear()
        self.table.field_id = field_id
        self.table.align = "c"
        self.table.add_rows(rows)
        print("all the tournament present sorted by ID")
        print(self.table)

    def display_all_tournament(self, tournaments):

        """
    Displays information about all tournaments in a table format, sorted by ID.
    Args:
        tournaments (list): A list of dictionaries, where each dictionary represents a tournament.
    Returns:
        None
    """

        display_field = self.display_header_tournament
        rows = []
        for tournament in tournaments:
            rows.append([
                tournament[field.lower()] for field in display_field
            ])
        self.table.clear()
        self.table.field_id = display_field
        self.table.align = "c"
        self.table.add_rows(rows)
        print("all the tournament present sorted by ID")
        print(self.table)

    def display_name_and_dates(self, tournmanent_name, start_date, end_date):

        """
        Displays the name and dates of a tournament.
        Args:
            tournmanent_name (str): The name of the tournament.
            start_date (str): The start date of the tournament.
            end_date (str): The end date of the tournament.
        Returns:
            None
        """

        print(f"tournament_name: {tournmanent_name}")
        print(f"start_date: {start_date}")
        print(f"end_date: {end_date}")

    def display_tournament(self, t):

        """
        Displays detailed information about a tournament.
        Args:
            t (dict): A dictionary representing a tournament.
        Returns:
            None
        """
        header = (f"id: {t['tournament_id']}, name: {t['tournament_name']}\n"
                  f"site: {t['tournament_site']}\n"
                  f"Rounds: {t['current_round']}/{t['number_of_rounds']}\n"
                  f"start_date: {t['start_date']}\n"
                  f"end_date: {t['end_date']}")
        print(header)

    def display_matches_report(self, round_num, all_matches):

        """
        Displays a report of all matches in a particular round.
        Args:
            round_num (int): The round number.
            all_matches (list): A list of lists, where each inner list contains information about a match.
        Returns:
            None
        """

        self.table.clear()
        self.table.field_names = self.matches_report_field_names
        self.table.align = "l"
        for i in range(len(all_matches)):
            all_matches[i].insert(3, "vs.")
            self.table.add_row(all_matches[i])
        print(f"Round {round_num}:")
        print(self.table)
