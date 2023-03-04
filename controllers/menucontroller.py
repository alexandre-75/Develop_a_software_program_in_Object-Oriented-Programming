from views.menuview import MainMenu
from views.playerview import PlayerView
from views.tournamentview import TournamentView

from views.reportview import ReportView

from controllers.tournamentcontrolleur import TournamentController
from controllers.reportcontroller import ReportController

from models.tournament import Tournament
from models.player import Player


class MenuController():

    def __init__(self):

        self.menu_view = MainMenu()
        self.tournament_view = TournamentView()
        self.player_view = PlayerView()
        self.report_view = ReportView()

        self.tournament_controller = TournamentController()
        self.report_controller = ReportController()

    def main_menu_start(self):

        """Starts the main menu and prompts the user to select an option. 
        Depending on the user's input, it calls one of the following methods:
        - creation_of_a_new_tournament()
        - creation_of_a_new_player()
        - load_an_old_profile()
        - update_player()
        - load_an_old_tournament()
        - report_menu()
        - exit_the_program()"""

        self.menu_view.print_main_menu_options()
        user_input = self.menu_view.enter_a_number_to_select_a_main_menu_option()
        if user_input == 1:
            self.creation_of_a_new_tournament()
        elif user_input == 2:
            self.creation_of_a_new_player()
        elif user_input == 3:
            self.load_an_old_profile()
        elif user_input == 4:
            self.update_player()
        elif user_input == 5:
            self.load_an_old_tournament()
        elif user_input == 6:
            self.report_menu()
        else:
            user_input == 7
            self.exit_the_program()

    def creation_of_a_new_player(self):
        
        """Prompts the user to enter player information, including their ID, name, date of birth, score, and ranking. 
        After entering the information, the user is asked to confirm the details before saving the player to the database.
        If the user confirms the information, the new player is saved, and the user is returned to the main menu. 
        If the user does not confirm the information, the method starts over and prompts the user to enter the information again.

        @param self: Instance of the class.
        @return: None."""

        player_information = {}
        options = {
            "player_id": "player id",
            "last_name": "last name",
            "first_name": "frist name",
            "date_of_birth": "Date of birth (DD-MM-YYYY)",
            "score_of_player": "score of player",
            "ranking": "ranking"
        }
        self.player_view.exit_save_player()
        for key, value in options.items():
            self.menu_view.ergonomics()
            if value == "player id":
                pass
            else:
                self.player_view.exit_save_player()
            user_input = ""
            user_input = input(f"{value}: ").lower()
            if user_input == "quit":
                if value == "player id":
                    self.player_view.exit_player_creation_or_continue()
                    user_input = input()
                    if user_input == "b":
                        self.main_menu_start()
                    else:
                        self.creation_of_a_new_player()
                else:
                    player = Player(**player_information)
                    player.save_player_in_database()
                    self.menu_view.ergonomics()
                    self.player_view.player_message_is_saved_in_the_database()
                    self.main_menu_start()
            else:
                player_information[key] = user_input
        self.player_view.summary_of_new_player_created(player_information)
        self.menu_view.ergonomics()
        user_input = input("Do you confirm player information ? (YES ou NO) ").lower()
        if user_input == "yes":
            player = Player(**player_information)
            player.save_player_in_database()
            self.player_view.player_message_is_saved_in_the_database()
            self.menu_view.ergonomics()
            self.main_menu_start()
        else:
            self.creation_of_a_new_player()

    def creation_of_a_new_tournament(self):

        """Create a new tournament by prompting the user to input various pieces of information about it, 
        including the tournament ID, name, site, number of rounds, current round, general remarks, and list of players.
        Once all the required information has been gathered and verified, the tournament 
        is saved to the database and a summary of the new tournament is displayed for the user's review. 
        If the user confirms the information, the tournament is officially created and the user is prompted to start the tournament.

        @Parameters: None
        @Return: None"""

        tournament_info = {}
        options = {
            "tournament_id": "Tournament ID",
            "tournament_name": "Tournament name",
            "tournament_site": "Tournament site",
            "current_round": "Current round",
            "number_of_rounds": "Number of rounds",
            "general_remarks": "General remarks"
        }
        self.player_view.exit_save_player()
        for key, value in options.items():
            self.menu_view.ergonomics()
            if value == "Tournament ID":
                pass
            else:
                self.player_view.exit_save_player()
            user_input =""
            user_input = input(f"{value}: ").lower()
            if user_input == "quit":
                if value == "Tournament ID":
                    self.tournament_view.exit_tournament_creation_or_continue()
                    user_input = input()
                    if user_input == "b":
                        self.main_menu_start()
                    else:
                        self.creation_of_a_new_tournament()
                else:
                    tournament = Tournament(**tournament_info)
                    tournament.save_tournament_in_database()
                    self.tournament_view.tournament_message_is_saved_in_the_database()
                    self.main_menu_start()
            else:
                tournament_info[key] = user_input
        player_present_in_the_tournament = self.tournament_controller.select_player_list(4)
        self.tournament_view.summary_of_new_tournament_created(tournament_info, player_present_in_the_tournament)

        user_input = input("Do you confirm tournament information? (YES or NO) : ").lower()
        if user_input == "yes":
            tournament = Tournament(
                tournament_id=tournament_info["tournament_id"],
                tournament_name=tournament_info["tournament_name"],
                tournament_site=tournament_info["tournament_site"],
                current_round=tournament_info["current_round"],
                number_of_rounds=tournament_info["number_of_rounds"],
                general_remarks=tournament_info["general_remarks"],
                start_date="_",
                end_date="_",
                players=player_present_in_the_tournament,
                rounds=[]
            )
            tournament.save_tournament_in_database()
            self.tournament_view.tournament_message_is_saved_in_the_database()
            self.tournament_view.message_start_tournament()
            user_input = input().lower()
            if user_input == "yes":
                self.tournament_controller.start_tournament(tournament)
                pass
            elif user_input == "no":
                self.main_menu_start()
        else:
            self.creation_of_a_new_tournament()

    def update_player(self):

        """Update a player's information in the database.
        @param self: The object pointer.
        @return: None."""

        players = Player.load_all_players_from_database()
        self.player_view.display_available_players(players)
        player_index = int(input("Enter a number to select the player: ")) - 1
        p = players[player_index]
        p = Player(
            p['last_name'],
            p['first_name'],
            p['date_of_birth'],
            p['player_id'],
            p['score_of_player'],
            p['ranking']
        )
        options = ["last_name", "first_name", "date_of_birth", "player_id", "score_of_player", "ranking"]
        self.player_view.display_player_update_options(options)
        option_index = int(input("Enter a number to select the option: ")) - 1
        new_value = None  # initialiser à None
        if option_index <= len(options):
            option = options[option_index]
            if option == "score_of_player" or option == "ranking":
                new_value = int(input(f"Entrez {option} : "))
            elif option == "player_id":
                self.menu_view.ergonomics()
                self.player_view.non_editable_value()
                self.update_player()
                return  # sauter le reste de la méthode
            else:
                new_value = input(f"Entrez {option} : ")
            p.update_player_in_database(option, new_value)
            self.player_view.player_message_is_saved_in_the_database()
            self.main_menu_start()
        else:
            self.player_view.player_message_not_saved_in_the_database()
            self.update_player()

    def exit_the_program(self):
        self.menu_view.quit_the_program_now()
        user_input = str(input()).lower()
        if user_input == "yes":
            exit()
        else:
            user_input == "no"
            self.main_menu_start()

    def load_an_old_tournament(self):
        tournament_list = Tournament.load_all_tournaments_from_database(self)
        self.tournament_view.select_tournament(tournament_list)
        user_input = str(input("enter a tournament ID : "))
        selected_tournament = None
        for tournament in tournament_list:
            if user_input == str(tournament["tournament_id"]):
                selected_tournament = tournament
                print(selected_tournament["rounds"])
                print(type(selected_tournament["rounds"]))
                print(len(selected_tournament["rounds"]))
                t = Tournament(
                    selected_tournament['tournament_id'],
                    selected_tournament['tournament_name'],
                    selected_tournament['tournament_site'],
                    selected_tournament['start_date'],
                    selected_tournament['end_date'],
                    selected_tournament['number_of_rounds'],
                    selected_tournament['current_round'],
                    selected_tournament['general_remarks'],
                    selected_tournament['rounds'],
                    selected_tournament['players'],
                )
                print("sssssssssssssssssssssssss")
                print(t.repr())
                print("ssssssssssssssssssssssssssssssss")
                a = Tournament.deserialize_tournament(self, selected_tournament)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(type(a))
                # print(a.tournam)
                self.tournament_controller.start_tournament(a)

    def report_menu(self):
        self.report_view.report_menu()
        user_input = self.menu_view.enter_a_number_to_select_a_report_option()
        if user_input == 1:
            self.report_controller.all_players_sorted_alphabetically(Player.load_all_players_from_database())
        if user_input == 2:
            self.report_controller.all_tournaments(Tournament.load_all_tournaments_from_database(self))
        if user_input == 3:
            self.report_controller.name_and_dates_of_a_tournament(Tournament.load_all_tournaments_from_database(self))
        if user_input == 4:
            self.report_controller.list_of_tournament(Tournament.load_all_tournaments_from_database(self))
        if user_input == 5:
            self.report_controller.list_all_matches_in_all_rounds(Tournament.load_all_tournaments_from_database(self))
    
    def load_an_old_profile(self):

        """Load an old player profile and allow the user to update the player's information in the database.
        @param self: The object pointer.
        @return: None."""

        player_list = Player.load_all_players_from_database()
        self.report_controller.all_players_sorted_alphabetically(player_list)
        user_input = input("enter a player id : ")
        for player in player_list:
            if player["player_id"] == user_input:
                options = ["last_name", "first_name", "date_of_birth", "player_id", "score_of_player", "ranking"]
                self.player_view.display_player_update_options(options)
                option_index = int(input("Enter a number to select the option: ")) - 1

                if option_index <= len(options):
                    option = options[option_index]
                    if option == "score_of_player" or option == "ranking":
                        new_value = int(input(f"Entrez {option} : "))
                    elif option == "player_id":
                        self.menu_view.ergonomics()
                        self.player_view.non_editable_value()
                        self.load_an_old_profile()
                    else:
                        new_value = input(f"Entrez {option} : ")
                        print("tata")

                    p = Player(
                        player['last_name'],
                        player['first_name'],
                        player['date_of_birth'],
                        player['player_id'],
                        player['score_of_player'],
                        player['ranking'])

                    p.update_player_in_database(option, new_value)
                    self.player_view.player_message_is_saved_in_the_database()
                    user_input_2 = str(input("do you still want to change a player's settings? [yes][no] "))
                    if user_input_2 == "yes":
                        self.load_an_old_profile()
                    else:
                        self.main_menu_start()

                else:
                    self.menu_view.ergonomics()
                    self.player_view.player_message_not_saved_in_the_database()
                    self.load_an_old_profile()
