class Player():
    def __init__(self, first_name, surname, date_of_birth,):
        self.first_name = first_name
        self.surname = surname
        self.date_of_birth = date_of_birth
    
    def __repr__(self):
        return f"Player({self.first_name}, {self.surname}, {self.date_of_birth})"

    def __str__(self):
        return f"(first name : {self.first_name}\n surname : {self.surname}\n date of birth : {self.date_of_birth})"
    

from faker import Faker
fake = Faker(locale="fr_FR")

for _ in range(10):
    player = Player(first_name = fake.first_name(), surname = fake.last_name(), date_of_birth = fake.date_of_birth())
    print(repr(player))
    print("-" * 10)
    # print(player)