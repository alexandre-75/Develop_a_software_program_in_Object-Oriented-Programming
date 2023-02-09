from views.playerview import PlayerView
from models.player import Player


class PlayerController:

    def __init__(self):
        self.view = PlayerView()
        
    def new_player(self):
        new_player = Player(self.view.input_first_name(),
                            self.view.input_last_name(), 
                            self.view.input_date_of_birth(),
                            self.view.input_player_id(),
                            self.view.input_score(),
                            self.view.input_rankig())
        return new_player