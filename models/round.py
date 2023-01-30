class Round:
    def __init__(self, name, beginning_date, ending_date):
        self.name = name
        self.beginning_date = beginning_date
        self.ending_date = ending_date
        self.match_list = []
    
    def add_match(self, match):
        self.match_list.append(match)