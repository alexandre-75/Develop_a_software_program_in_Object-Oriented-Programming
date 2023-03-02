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
        self.table.clear()
        self.table.field_names = self.round_field_names

        for i in range(len(matches)):
            row = list(matches[i])
            row.insert(0, str(i+1))
            row.insert(4, "vs.")

            self.table.add_row(row)

        print(self.table)

    def score_options(self, match_number):
        print("Match : ", int(match_number) + 1)
        print('[1] Draw')
        print('[2] Player 1 wins')
        print('[3] Player 2 wins')
