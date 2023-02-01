from tinydb import TinyDB

class Match():

    db_match = TinyDB("database/match.json", indent=4)

    def __init__(self, player_1, score_player_1, player_2, score_player_2):
        self.player_1 = player_1
        self.score_player_1 = score_player_1
        self.player_2 = player_2
        self.score_player_2 = score_player_2
        self.match_result = ([player_1, score_player_1], [player_2, score_player_2])
 
    def __str__(self):
        return f"{self.player_1} contre {self.player_2}"

    def __repr__(self):
        return f"Match({self.player_1}, {self.player_2})"

    def save_match_in_db(self):
        match_json_format = {"match_result": self.match_result}
        return Match.db_match.insert(match_json_format)


from faker import Faker
fake = Faker(locale="fr_FR")
scores = [75, 80, 85, 90, 95, 100]
for _ in range(10):
    match = Match(
        player_1 = fake.first_name(),
        player_2 = fake.first_name(), 
        score_player_1 = fake.random_element(elements=scores),
        score_player_2 = fake.random_element(elements=scores))
    print(match.save_match_in_db())


