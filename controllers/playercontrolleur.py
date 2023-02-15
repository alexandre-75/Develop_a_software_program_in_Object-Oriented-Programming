from views.menuview import MainMenu
from views.playerview import PlayerView
from models.player import Player

class PlayerControlleur():
    def __init__(self):
        self.menu_view = MainMenu()
        self.player_view = PlayerView()

    def new_player(self):
        self.player_view.display_new_player()
        player_info =[]
        options = ["first_name","last_name","date of birth","player_id","score_player","rank"]
        for i in options:
            self.menu_view.input_prompt_text_2(i)
            user_input = input()
            player_info.append(user_input)
        self.player_view.review_player(player_info)
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
            self.player_view.player_saved()
            self.main_menu_start()
        elif user_input == "no":
            self.main_menu_start()

def update_player(self):
        players = Player.load_all_players_from_database()
        while True:
            self.player_view.select_players(players)
            player_index = self.menu_view.input_a_number() - 1
            selected_player = players[player_index]
            options = ["first_name", "last_name", "date_of_birth", "player_id", "score_of_player", "rank"]
            while True:
                self.player_view.update_player_info(selected_player, options)
                option_index = self.menu_view.input_a_number() - 1
                selected_option = options[option_index]
                new_value = self.menu_view.input_prompt_text(f"nouveau {options[option_index]}")
                selected_player[selected_option] = new_value
                selected_player.update_player_in_database(selected_option, new_value, selected_player.player_id)
                self.player_view.player_saved()
                break