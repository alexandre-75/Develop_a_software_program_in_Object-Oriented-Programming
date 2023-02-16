from views.menuview import MainMenu
from controllers.playercontrolleur import PlayerControlleur
from controllers.tournamentcontrolleur import TournamentController

menu_view = MainMenu()
player_controller = PlayerControlleur()
tournament_controller = TournamentController()

def main_menu_start():
    menu_view.display_main_menu()
    user_input = menu_view.input_a_number()
    print(user_input)
    if user_input == 1:
        tournament_controller.new_tournament()
    elif user_input == 2:
        player_controller.new_player()
    elif user_input == 3:
        player_controller.update_player()
    elif user_input == 4:
        tournament_controller.load_an_old_tournament()
    else: 
        user_input == 5
        menu_view.exit_the_program()
        user_input = str(input()).lower()
        if user_input == "yes":
            exit()
        else:
            user_input == "no"
            main_menu_start()

main_menu_start()