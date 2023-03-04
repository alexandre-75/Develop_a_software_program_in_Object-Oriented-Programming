from prettytable import PrettyTable


class RoundView():

    def __init__(self):
        self.table = PrettyTable()
        self.round_field_names = [
            "Match #",
            "Name P1",
            "Rank P1",
            "Score P1",
            " ",
            "Name P2",
            "Rank P2",
            "Score P2"
        ]

    def display_matches(self, matches):

        """
         Displays a PrettyTable table with the matches passed as parameters. Each line represents a match
         with match number, player 1 name, ranking, score, "vs.", player 2 name,
         their ranking and score.
        
         args:
             matches (list): A list of tuples, each tuple contains the information of a match
                             (name of players, ranking, score).
         """
         
        self.table.clear()
        self.table.field_names = self.round_field_names
        for i in range(len(matches)):
            row = list(matches[i])
            row.insert(0, str(i+1))
            row.insert(4, "vs.")
            self.table.add_row(row)
        print(self.table)

    def score_options(self, match_number):

        """
         Displays scoring options for a given match.
        
         args:
             match_number (int): The match number to display scoring options for.
         """
        print("Match : ", int(match_number) + 1)
        print('[1] Draw')
        print('[2] Player 1 wins')
        print('[3] Player 2 wins')
