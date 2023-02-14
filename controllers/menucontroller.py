from views.menuview import MainMenu
from models.player import Player

class controllers():

    def __init__(self):
        self.menu_view = MainMenu()
    
    @staticmethod
    def main_menu_start(self):
        self.menu_view.display_main_menu()
        self.menu_view.input_a_number()
        user_input = str(input()).lower()
        if user_input == "1":
            self.new_tournament()
        elif user_input == "2":
            self.new_player()
        elif user_input == "3":
            self.menu_view.exit_the_program()
            user_input = str(input()).lower()
            if user_input == "yes":
                exit()
            elif user_input == "no":
                self.main_menu_start()
     
    
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

    def new_tournament(self):
            pass