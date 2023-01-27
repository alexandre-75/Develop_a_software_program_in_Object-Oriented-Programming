DEFAULT_ROUNDS = 4

class tournament():
    def __init__(
            self,
            tournament_name,
            site_of_tournament,
            start_date,
            end_date,
            current_round,
            list_of_tours,
            list_of_registered_players,
            description_for_general_remarks,
            number_of_rounds = DEFAULT_ROUNDS):

        self.tournament_name = tournament_name
        self.site_of_tournament = site_of_tournament
        self.start_date = start_date
        self.end_date = end_date
        self.current_round = current_round
        self.list_of_tours = list_of_tours
        self.list_of_registered_players = list_of_registered_players
        self.description_for_general_remarks = description_for_general_remarks
        self.number_of_rounds = number_of_rounds

