
class tournamentView():
    def input_for_tournament():
            
            tournament_name = input("Nom du tournoi: ")
            tournament_site = input("Lieu du tournoi: ")
            tournament_start_date = input(" début du tournoi: ")
            general_remarks = input("remarques: ")

            while True:
                try:
                    tournament_rounds = int(input("Nombre de tours: "))
                    if tournament_rounds == 0:
                        raise ValueError()
                    break
                except ValueError:
                    print("Attention ! Vous devez saisir un entier supérieur à 1 !")

            return {
                "name": tournament_name,
                "location": tournament_location,
                "date": tournament_date,
            }