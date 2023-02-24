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
     Selects a specified number of players from the database of all players.
     args:
         num_players (int): The number of players to select.  
     Returns:
         list: A list of dictionaries representing the selected players.   
     Raises:
         None
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
        return  self.selected_players
    
    def start_tournament(self, tournament):
        if tournament.current_round == 1:
            tournament.start_date = get_times()
            tournament.update_timer(tournament.start_date, 'start_date', tournament.tournament_id)
            self.round_one_tournament(tournament)
            tournament.current_round += 1
            print(tournament.update_tournament_db())
        elif 1 < tournament.current_round <= tournament.number_of_rounds:
            pass
        else: 
            tournament.current_round > tournament.number_of_rounds
            pass
    
    def round_one_tournament(self,tournament):
        round = Round("round1", get_times())
        a = self.selected_players
        b = len(a) // 2
        # print(len(a))
        top_players, bottom_players = tournament.split_players(a)
        # print(top_players)
        # print(bottom_players)
        for i in range(int(b)):
            round.add_match_to_list(top_players[i], bottom_players[i])
            top_players[i], bottom_players[i] = self.update_adversary(top_players[i], bottom_players[i])
        self.round_view.display_matches(round.matches_list)
        user_input = str(input("when the round is over enter [a] or else enter [b] ")).lower()
        scores_list = []
        if user_input == "a":
            round.end_date = get_times()
            tournament.rounds.append(round.all_information_round())
            # print(tournament.rounds)
            self.end_of_round(scores_list, tournament)

        elif user_input == "b":
            self.back_to_menu()

    @staticmethod
    def update_adversary(top_players, bottom_players):
        top_players["adversary"].append(bottom_players["player_id"])
        bottom_players["adversary"].append(top_players["player_id"])
        # print(player_1)
        return top_players, bottom_players

    @staticmethod
    def back_to_menu():
        from controllers.menucontroller import MenuController
        MenuController().main_menu_start()

    def end_of_round(self, scores_list: list, tournament):
        a = self.selected_players
        b = len(a) // 2
        for i in range(int(b)): 
            self.round_view.score_options(i)
            user_input = input(" entrer un score")
            # response = self.input_scores()
            scores_list = self.get_score(user_input, scores_list)
            print(scores_list)

        tournament.players = self.update_scores(a, scores_list)
        print("----------------------")
        print(tournament.players)
        return tournament.players

    def get_score(self, user_input, scores_list: list):
        if user_input == "0":
            scores_list.extend([0.5, 0.5])
            return scores_list
        elif user_input == "1":
            scores_list.extend([1.0, 0.0])
            return scores_list
        elif user_input == "2":
            scores_list.extend([0.0, 1.0])
            return scores_list
        else:
            pass
       
    @staticmethod
    def update_scores(players, scores_list: list):
        print("hello")
        for i in range(len(players)):
            players[i]["score_of_player"] += scores_list[i]
            print("nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn")
            # print[i]["score_of_player"]
        print(players)
        return players

   


    
 