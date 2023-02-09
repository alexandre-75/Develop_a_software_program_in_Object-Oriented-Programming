from models.player import Player
import string
from datetime import datetime

class PlayerView():
 
    def input_first_name(self):
        special_characters = string.punctuation + string.digits
        first_name = input("first name : ")
        if first_name.strip() and all(i not in special_characters for i in first_name):
            self.first_name = str(first_name)
        else:
            print("The first name can only contain alphabetic characters and must not be empty")
            self.input_first_name()
    
    def input_last_name(self):
        special_characters = string.punctuation + string.digits
        last_name = input("last name : ")
        if last_name.strip() and all(i not in special_characters for i in last_name):
            self.last_name = str(last_name)
        else:
            print("The last name can only contain alphabetic characters and must not be empty")
            self.input_last_name()
     
    def input_date_of_birth(self):
        date_of_birth = input("Date of birth (format YYYY-MM-DD :")
        try:
            date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d")
            self.date_of_birth = str(date_of_birth)
        except ValueError:
            print("Invalid format. Use YYYY-MM-DD")
            self.input_date_of_birth()

    def input_player_id(self):
        player_id = input("id: ")
        if len(player_id) == 7 and player_id[:2].isalpha() and player_id[2:].isdigit():
            self.player_id = str(player_id)
        else:
            print("Player ID must start with two letters followed by five digits")
            self.input_player_id()

    def input_ranking(self):
        ranking = input("ranking :")
        if ranking > 0 and ranking.isdigit():
            self.ranking = int(ranking)
        else:
            print("must be an integer greater than or equal to 1")
            self.input_rankig()

    def input_new_ranking_(self, player):  
        print(player)
        while True:
            try:
                new_ranking = int(input("Enter the new rating for the player above:"))
                if new_ranking < 0:
                    raise ValueError
            except ValueError:
                print("Il faut saisir un entier positif !")
            else:
                break
        return new_ranking

    def input_score(self):
        score = input("enter a positive score:")
        if score > 0 :
            self.score = int(score)
        else:
            print("must be than or equal to 1")

    def show_player(self, players):
        print(players)
    
    def input_list_id_players(self, max_players):
        player_ids = []
        for player_index in range(1, 9):
            player_id = input("player id" + str(player_index) + ": ")
            while True:
                try:
                    player_id = int(player_id)
                    if player_id > max_players or player_id < 0:
                        raise ValueError
                    if player_id in player_ids:
                        raise ArithmeticError
                    break
                except ValueError:
                    print("positive integer and less than the maximum number of stored players:" + str(max_players))
                    player_id = input("player id" + str(player_index) + ": ")
                except ArithmeticError:
                    print("This player is already in the list")
                    player_id = input("player id" + str(player_index) + ": ")
            player_ids.append(player_id)
        return player_ids
