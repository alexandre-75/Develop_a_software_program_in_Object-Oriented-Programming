class Player():
    def __init__(self, first_name, surname, date_of_birth, national_chess_identifier):
        self.first_name = first_name
        self.surname = surname
        self.date_of_birth = date_of_birth
        self.national_chess_identifier = national_chess_identifier
    
    def player_personal_information (self):
        information = {
            "first_name" : self.first_name,
            "surname" : self.surname,
            "date_of_birth" : self.date_of_birth,
            "national_chess_identifier" : self.national_chess_identifier,
        }
        return information
