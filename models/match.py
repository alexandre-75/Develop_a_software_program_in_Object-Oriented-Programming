from tinydb import TinyDB

class Match():

    matches_database = TinyDB("database/matches.json", indent=4)
  
    def __init__(self, match_id, player_1, score_p1, player_2, score_p2):
        self.match_id = match_id
        self.player_1 = player_1
        self.score_p1 = score_p1
        self.player_2 = player_2
        self.score_p2 = score_p2  
        self.result = ([player_1, score_p1], [player_2, score_p2])   # single match stored as a tuple containing two lists

    def __str__(self):
        return f"Match ID:{self.match_id}\n {self.player_1} vs {self.player_2}"

    def __repr__(self):
        return f"Match({self.player_1}, {self.player_2})"

    def format_match_in_data(self):
        return {"match_id": self.match_id,
                "result": self.result
        }

    def save_match_in_database(self):
            return self.matchs_database.insert(self.format_match_in_data())
 
    @staticmethod   # can be called without creating an instance of the class
    def find_match_in_database(match_id):
        matches_database = TinyDB('database/matches.json')
        result = matches_database.search(where("match_id") == match_id)   # Search in the database, the match corresponding to the id provided as input.
        if result == True:
            return result[0]
        return "No match in database"

    @staticmethod
    def update_match_in_database(key, value, match_id):
        matches_database = TinyDB('database/matches.json')
        match = self.find_match_in_database(match_id)
        if match == True:
            return matches_database.update({key:value}, where("match_id") == match_id)    
        return "Error in parameters"

    @staticmethod
    def load_all_matches_from_db():
        matches_database = TinyDB('database/matches.json')
        return matches_database.all()


# from faker import Faker
# fake = Faker(locale="fr_FR")
# scores = [75, 80, 85, 90, 95, 100]
# test_m_id= [0, 1, 2, 3, 4]
# for _ in range(10):
#     match = Match(
#         m_id= fake.random_element(elements=test_m_id),
#         player_1 = fake.first_name(),
#         player_2 = fake.first_name(), 
#         score_player_1 = fake.random_element(elements=scores),
#         score_player_2 = fake.random_element(elements=scores))
    # print(match.save_match_in_db())
    # print(match.__str__())
    # print("_"*10)


