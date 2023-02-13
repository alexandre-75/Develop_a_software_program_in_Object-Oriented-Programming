
from models.tournament import Tournament
from utils.date_and_time import get_timestamp

class TournamentView(Tournament):
    def __init__(self, tournament_id=False, tournament_name=False, tournament_site=False, start_date=False, end_date=false, number_of_rounds=4, general_remarks=""):

        super().__init__(tournament_id, tournament_name, tournament_site, start_date, end_date, number_of_rounds=4, current_round=1, general_remarks="")

    def input_tournament_id(self):
        self.player_id = str(input("id: "))

    def input_name(self):
        self.tournament_name = str(input("Quelle est le nom du tournoi ? : "))

    def input_tournament_site(self):
        self.tournament_site = str(input("Où ce déroule le tournoi ? : "))

    def start_date(self):
        date = get_timestamp()
        self.start_date = "date début tournoi" + date

    def input_number_of_rounds(self):
        self.number_of_rounds = int(input("Combien de tour ? : "))

    def input_general_remarks(self):
        self.general_remarks = input("Votre description : ")

    def how_many_player():
        return input("Combien de joueur vont participer au tournoi ?(inscrire un nombre pair et au minimum 4):")

    def wich_player_will_play():
        return input("Sélectionner un joueur à ajouter au tournoi avec son numéro. ")

    def display_tournament(self):
        print(
            f"""Récapitulatif :
        Nom du tournoi: {self.tournament_name}
        Localisation: {self.tournament_site}
        Nombre de tour: {self.number_of_rounds}
        Description: {self.general_remarks}
        date de début: {self.start_date}"""
        )