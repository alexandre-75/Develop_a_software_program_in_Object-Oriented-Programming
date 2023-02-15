from views.menuview import MainMenu
from controllers.playercontrolleur import PlayerControlleur
from controllers.tournamentcontrolleur import TournamentController

class controllers():

    def __init__(self):
        self.menu_view = MainMenu()
        self.player_controller = PlayerControlleur()
        self.tournament_controller = TournamentController()
    
    @staticmethod
    def main_menu_start(self):
        self.menu_view.display_main_menu()
        self.menu_view.input_a_number()
        user_input = str(input()).lower()
        if user_input == "1":
            self.player_controller.new_tournament()
        elif user_input == "2":
            self.tournament_controller.new_player()
        elif user_input == "3":
            self.player_controller.update_player()
        elif user_input == "4":
            self.menu_view.exit_the_program()
            user_input = str(input()).lower()
            if user_input == "yes":
                exit()
            elif user_input == "no":
                self.main_menu_start()