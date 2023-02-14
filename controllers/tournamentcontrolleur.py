
from views.menuview import MainMenu
from models.tournament import Tournament

class TournamentController():

    def __init__(self):
        self.menu_view = MainMenu()

    def new_tournament(self):
        self.menu_view.display_new_tournament()
        tournament_info =[]
        options ["tournament_id","tournament_name","tournament_site","number_of_rounds","general_remarks"]
        for i in options:
            self.menu_view.input_prompt_text(i)
            user_input = input()
            tournament_info.append(user_input)
        
        tours_players = self.select_players(8)
        self.menu_view.review_tournament(tournament_info, tours_players)
        user_input = input().lower()
        if user_input == "yes":
            tournament = Tournament(
                tournament_id=tournament_info[0],
                tournament_name=tournament_info[1],
                tournament_site=tournament_info[2],
                number_of_rounds=tournament_info[3],
                general_remarks=tournament_info[4],
                start_date="",
                end_date="",
                player=tours_players,
                current_round=1,
                rounds=[]    
            )
            tournament.save_tournament_in_database()
            self.menu_view.tournament_saved()
            self.menu_view.start_tournament_prompt()
            user_input = input()
            if user_input == "yes":
                pass
            elif user_input == "no":
                self.main_menu_start()
    

    def select_players(self, players_total):
        players = Player.load_all_players_from_database()
        id_list = []
        for i in range(len(players)):
            id_list.append(players[i]["player_id"])
        tour_players = []
        i = 0
        while i < players_total:
            self.menu_view.select_players(players, i+1)
            self.menu_view.input_prompt()
            user_input = input()
            if int(user_input) in id_list:
                index = id_list.index(int(user_input))
                tour_players.append(players[index])
                id_list.pop(index)
                i += 1
            else:
                self.menu_view.player_already_selected()
        return tour_players