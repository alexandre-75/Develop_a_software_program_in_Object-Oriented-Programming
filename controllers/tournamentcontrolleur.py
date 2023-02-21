from models.player import Player

from views.playerview import PlayerView
from views.tournamentview import TournamentView

class TournamentController():

    def __init__(self):

        self.player_view = PlayerView()
        self.tournament_view = TournamentView()

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
        selected_players = []
        player_ids = [p['player_id'] for p in players]
        for i in range(num_players):
            valid_input = False
            while not valid_input:
                self.player_view.display_available_players(players)
                player_id = input("Enter the ID of player #{0}: ".format(i+1))
                if player_id in player_ids:
                    player = players[player_ids.index(player_id)]
                    selected_players.append(player)
                    players.remove(player)
                    player_ids.remove(player_id)
                    valid_input = True
                else:
                    self.tournament_view.invalid_player_id()
                    selected_players
        return selected_players