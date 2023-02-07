from models.player import Player

class PlayerView():

    def __init__(self,first_name=False, last_name=False, date_of_birth=False, player_id=False):
 
        super().__init__(first_name, last_name, date_of_birth, player_id)

    def input_first_name(self):
        self.first_name = str(input("Quelle est le prénom du joueur ? : "))

    def input_last_name(self):
        self.last_name = str(input("Quelle est le nom du joueur ? : "))

    def input_date_of_birth(self):
        self.date_of_birth = str(input("Date de naissance (format YYYY-MM-DD) :"))

    def input_player_id(self):
        self.player_id = str(input("id: "))

    def display_player(self):
        print(f"Récapitulatif:\n Id: {self.player_id}\n Nom: {self.last_name}\n Prénom: {self.first_name}\n Date de naissance: {self.date_of_birth}")

    def display_added_player_message(self):
        print(f"{self.last_name} {self.first_name} est ajouté.")
    
