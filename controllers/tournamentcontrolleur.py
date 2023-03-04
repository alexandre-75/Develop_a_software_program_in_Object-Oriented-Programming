from models.player import Player
from models.round import Round

from views.playerview import PlayerView
from views.tournamentview import TournamentView
from views.roundview import RoundView

from utils.date_and_time import get_times


class TournamentController():

    def __init__(self):

        self.player_view = PlayerView()
        self.tournament_view = TournamentView()
        self.round_view = RoundView()
        self.selected_players = []

    def select_player_list(self, num_players):

        """
        Selects a list of players for a tournament, based on user input.
        @param num_players: An integer representing the number of players to select.
        @return: A list of dictionaries, each representing a selected player.
        """

        players = Player.load_all_players_from_database()
        player_ids = [p['player_id'] for p in players]
        for i in range(num_players):
            valid_input = False
            while not valid_input:
                self.player_view.display_available_players(players)
                player_id = input("Enter the ID of player #{0}: ".format(i+1))
                if player_id in player_ids:
                    player = players[player_ids.index(player_id)]
                    self.selected_players.append(player)
                    players.remove(player)
                    player_ids.remove(player_id)
                    valid_input = True
                else:
                    self.tournament_view.invalid_player_id()
        self.selected_players
        return self.selected_players

    def start_tournament(self, tournament):

        """
        Starts the tournament by running all rounds, updating the start and end dates,
        and displaying a farewell message.
        @param tournament: A dictionary representing the tournament to start.
        """

        if tournament.current_round == 1:
            tournament.start_date = get_times()
            tournament.update_timer(tournament.start_date, 'start_date', tournament.tournament_id)
            self.round_tournament(tournament, tournament.current_round)
            tournament.update_tournament_from_database()
            tournament.current_round += 1
            while tournament.current_round <= tournament.number_of_rounds:
                self.next_rounds(tournament)
                tournament.update_tournament_from_database()
                tournament.current_round += 1
            tournament.end_date = get_times()
            tournament.update_timer(tournament.end_date, 'end_date', tournament.tournament_id)
            print("tournament finished goodbye")
        else:
            1 < tournament.current_round <= tournament.number_of_rounds
            while tournament.current_round <= tournament.number_of_rounds:
                #
                tournament.current_round += 1
                tournament.update_tournament_from_database()
            tournament.end_date = get_times()
            tournament.update_timer(tournament.end_date, 'end_date', tournament.tournament_id)
            print("tournament finished goodbye")

    def round_tournament(self, tournament, round_number):

        """
        Runs a single round of the tournament by pairing up players, creating matches, and updating scores.
        @param tournament: A dictionary representing the tournament to round.
        @param round_number: An integer representing the current round number.
        """

        round = Round(f"round{round_number}")
        a = self.selected_players
        b = len(a) // 2
        top_players, bottom_players = tournament.split_players(a)
        for i in range(int(b)):
            round.add_match_to_list(top_players[i], bottom_players[i])
            top_players[i], bottom_players[i] = self.update_adversary(top_players[i], bottom_players[i])
        self.round_view.display_matches(round.matches_list)
        user_input = str(input("when the round is over enter [a] or else enter [b] ")).lower()
        scores_list = []
        if user_input == "a":
            tournament.rounds.append(round.all_information_round())
            self.update_scores_and_return_players(scores_list, tournament)
        elif user_input == "b":
            self.back_to_menu()

    @staticmethod
    def update_adversary(top_players, bottom_players):

        """
        Updates the adversary attribute of two players to include each other's IDs.
        @param top_players: A dictionary representing the player with a higher score.
        @param bottom_players: A dictionary representing the player with a lower score.
        @return: A tuple containing the updated dictionaries.
        """

        top_players["adversary"].append(bottom_players["player_id"])
        bottom_players["adversary"].append(top_players["player_id"])
        return top_players, bottom_players

    @staticmethod
    def back_to_menu():
        from controllers.menucontroller import MenuController
        MenuController().main_menu_start()

    def update_scores_and_return_players(self, scores_list, tournament):

        """
        Updates the scores of the players in a tournament based on user input, and returns the updated player list.
        @param scores_list: A list of integers representing the scores for each match.
        @param tournament: A dictionary representing the tournament to update.
        @return: A list of dictionaries representing the updated player list.
        """

        a = self.selected_players
        b = len(a) // 2
        for i in range(int(b)):
            self.round_view.score_options(i)
            user_input = input("enter a number [1] [2] or [3] : ")
            scores_list = self.get_score(user_input, scores_list)
        tournament.players = self.update_scores_of_players(a, scores_list)
        return tournament.players

    def get_score(self, user_input, scores_list):

        """
        Given user input, updates a list of scores with the appropriate score based on the input.    
        @param user_input: A string representing the user's input for the score.
        @param scores_list: A list of integers representing the scores for each match.
        @return: A list of integers representing the updated scores.
        """

        score_dict = {"1": [0.5, 0.5], "2": [1.0, 0.0], "3": [0.0, 1.0]}
        if user_input in score_dict:
            scores_list.extend(score_dict[user_input])
        return scores_list

    def update_scores_of_players(self, players, scores_list):

        """
        Updates the scores of players based on the scores in the provided list.
        
        @param players: A list of dictionaries representing the players.
        @param scores_list: A list of integers representing the scores for each match.
        @return: A list of dictionaries representing the updated players.
        """

        for i in range(len(players)):
            players[i]["score_of_player"] += scores_list[i]
        return players

    def next_rounds(self, tournament):

        """
        Play the next round of the tournament.
        Args: tournament (Tournament): The tournament object to play the round for.
        Returns: None
        """

        round = Round("round " + str(tournament.current_round))
        a = tournament.sort_players_by_score()
        b = len(a) // 2
        top_players, bottom_players = tournament.split_players(a)
        for i in range(int(b)):
            round.add_match_to_list(top_players[i], bottom_players[i])
            top_players[i], bottom_players[i] = self.update_adversary(top_players[i], bottom_players[i])
        self.round_view.display_matches(round.matches_list)
        user_input = str(input("when the round is over enter [a] or else enter [b] ")).lower()
        scores_list = []
        if user_input == "a":
            tournament.rounds.append(round.all_information_round())
            self.update_scores_and_return_players(scores_list, tournament)
        elif user_input == "b":
            self.back_to_menu()

    @staticmethod
    def update_player_lists(player_1, player_2, available_list, players_added):

        """
        Static method to update the available list of players and the list of players added to a tournament.
        Args:
        player_1 (dict): The first player to be added.
        player_2 (dict): The second player to be added.
        available_list (list): A list of available players.
        players_added (list): A list of players already added to the tournament.
        Returns:
        tuple: A tuple containing the updated available list and the list of players added.
        """
        
        players_added.extend([player_1, player_2])
        available_list.remove(player_1)
        available_list.remove(player_2)
        return available_list, players_added
