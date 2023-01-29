import string
from datetime import datetime

class Player():
    def __init__(self, first_name, surname, date_of_birth):
        self.first_name = first_name
        self.surname = surname
        self.date_of_birth = date_of_birth
    
    def __repr__(self):
        return f"Player({self.first_name}, {self.surname}, {self.date_of_birth})"

    def __str__(self):
        return f"(first name : {self.first_name}\n surname : {self.surname}\n date of birth : {self.date_of_birth})"

    def _check_first_name_and_surname(self):
        special_characters = string.punctuation + string.digits
        if not (self.first_name and self.surname):
            raise ValueError("first name and last name cannot be empty.")
        for i in self.first_name:
            if i in special_characters:
                raise ValueError(f"not valid : {self.first_name}")
        for i in self.surname:
            if i in special_characters:
                raise ValueError(f"not valid : {self.surname}")

    def _check_date_of_birth(self):
        try:
            datetime.strptime(str(self.date_of_birth),'%Y-%m-%d')
        except:
            raise ValueError("Invalid format. Use YYYY-MM-DD")

from faker import Faker
fake = Faker(locale="fr_FR")

for _ in range(10):
    player = Player(first_name = fake.first_name(), surname = fake.last_name(), date_of_birth = fake.date_of_birth())
    player._check_first_name_and_surname()
    player._check_date_of_birth()
    print(repr(player))
    print("-" * 10)
    print(player)