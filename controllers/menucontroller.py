from views.menuview import MainMenu

class controllers():

    def __init__(self):
        self.menu_view = MainMenu()
    
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

  



        
    def new_tournament(self):
        pass
    def new_player(self):
        pass