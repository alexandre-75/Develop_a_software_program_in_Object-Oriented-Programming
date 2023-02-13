from views.playerview import PlayerView
from models.player import Player


class PlayerController:

    def __init__(self):
        self.view = PlayerView()
         self.players = {}
        
    def new_player(self):
        new_player = Player(self.view.input_first_name(),
                            self.view.input_last_name(), 
                            self.view.input_date_of_birth(),
                            self.view.input_player_id(),
                            self.view.input_score(),
                            self.view.input_rankig())
        self.players[new_player.player_id] = new_player
        return new_player
    

    def __str__(self):
        liste_joueur = ''
        for player_id, player in self.players.items():
            liste_joueur += f"joueur {player_id}: {player}\n"
        return liste_joueur

    def __getitem__(self, key):
        return self.players[key]

    def __setitem__(self, key, value):
        if key in self.players:
            self.players[key] = value
        else:
            self.players[key] = value