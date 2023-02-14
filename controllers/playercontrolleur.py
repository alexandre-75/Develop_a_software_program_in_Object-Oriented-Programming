from views.menuview import MainMenu
from models.player import Player

class PlayerControlleur():
    def __init__(self):
        self.menu_view = MainMenu()

    def new_player(self):
        self.menu_view.display_new_player()
        player_info =[]
        options = ["first_name","last_name","date of birth","player_id","score_player","rank"]
        for i in options:
            self.menu_view.input_prompt_text(i)
            user_input = input()
            player_info.append(user_input)
        MainMenu.review_player(player_info)
        user_input = input().lower()
        if user_input == "yes":
            player = Player(
                last_name=player_info[0],
                first_name=player_info[1],
                date_of_birth=player_info[2],
                player_id=player_info[3],
                score_player=player_info[4],
                ranking=player_info[5]
            )
            player.save_player_in_database()
            self.menu_view.player_saved()
            self.main_menu_start()
        elif user_input == "no":
            self.main_menu_start()