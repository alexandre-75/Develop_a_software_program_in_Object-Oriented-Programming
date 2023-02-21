from views.menuview import MainMenu
from views.playerview import PlayerView
from views.tournamentview import TournamentView
from views.roundview import RoundView

from controllers.tournamentcontrolleur import TournamentController

from models.tournament import Tournament
from models.player import Player
from models.round import Round


class MenuController():

    def __init__(self):

        self.menu_view = MainMenu()
        self.tournament_view = TournamentView()
        self.player_view = PlayerView()
        self.round_view = RoundView()

        self.tournament_controller = TournamentController()
        

    def main_menu_start(self):
        self.menu_view.print_main_menu_options()
        user_input = self.menu_view.enter_a_number_to_select_a_main_menu_option()
        print(user_input)
        if user_input == 1:
            self.creation_of_a_new_tournament()
        elif user_input == 2:
            self.creation_of_a_new_player()
        elif user_input == 3:
            self.update_player()
        elif user_input == 4:
            self.tournament_controller.load_an_old_tournament()
        else: 
            user_input == 5
            self.menu_view.quit_the_program_now()
            user_input = str(input()).lower()
            if user_input == "yes":
                exit()
            else:
                user_input == "no"
                main_menu_start()
         

    def creation_of_a_new_player(self):
        player_information= {}
        options = {
            "first_name": "frist name",
            "last_name": "last name",
            "date_of_birth": "Date of birth (DD-MM-YYYY)",
            "player_id": "player id",
            "score_of_player": "score of player",
            "ranking": "ranking"
        }
        for key, value in options.items():
            user_input = ""
            while not user_input:
                user_input = input(f"{value}: ")
            player_information[key] = user_input
        self.player_view.summary_of_new_player_created(player_information)
        user_input = input("Do you confirm player information ? (YES ou NO) ").lower()
        if user_input == "yes":
            player = Player(**player_information)
            player.save_player_in_database()
            self.player_view.player_message_is_saved_in_the_database()
            self.main_menu_start()
        else:
            self.creation_of_a_new_player()
        
    def creation_of_a_new_tournament(self):
        tournament_info = {}
        options = {
            "tournament_id": "Tournament ID",
            "tournament_name": "Tournament name",
            "tournament_site": "Tournament site",
            "current_round": "Current round",
            "number_of_rounds": "Number of rounds",
            "general_remarks": "General remarks"
        }
        for key, value in options.items():
            user_input = input(f"{value}: ")
            tournament_info[key] = user_input
        
        player_present_in_the_tournament = self.tournament_controller.select_player_list(2)
        self.tournament_view.summary_of_new_tournament_created(tournament_info, player_present_in_the_tournament)
        
        user_input = input("Do you confirm tournament information? (YES or NO)").lower()
        if user_input == "yes":
            tournament = Tournament(
                tournament_id=tournament_info["tournament_id"],
                tournament_name=tournament_info["tournament_name"],
                tournament_site=tournament_info["tournament_site"],
                current_round=tournament_info["current_round"],
                number_of_rounds=tournament_info["number_of_rounds"],
                general_remarks=tournament_info["general_remarks"],
                start_date="_",
                end_date="__",
                players= player_present_in_the_tournament,
                rounds=[]    
            )
            tournament.save_tournament_in_database()
            self.tournament_view.tournament_message_is_saved_in_the_database()
            self.tournament_view.message_start_tournament()
            user_input = input().lower()
            if user_input == "yes":
                # self.tournament_controller.start_tournament(tournament)
                pass
            elif user_input == "no":
                self.main_menu_start()
        else:
            self.new_tournament()