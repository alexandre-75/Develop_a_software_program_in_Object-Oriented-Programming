from tinydb import TinyDB

class Match():

    db_match = TinyDB("database/match.json", indent=4)

    def __init__(self, m_id, player_1, score_player_1, player_2, score_player_2):
        self.m_id = m_id
        self.player_1 = player_1
        self.score_player_1 = score_player_1
        self.player_2 = player_2
        self.score_player_2 = score_player_2  
        self.match_result = ([player_1, score_player_1], [player_2, score_player_2])   # single match stored as a tuple containing two lists
 
    def __str__(self):
        return f"match ID:{self.m_id}\n {self.player_1} contre {self.player_2}"

    def __repr__(self):
        return f"Match({self.player_1}, {self.player_2})"

    def format_match_data(self):
        return {"match_ID": self.m_id,
                "match_result": self.match_result}

    def save_match_in_db(self):
            return self.db_match.insert(self.format_match_data())
 
    @staticmethod
    def search_match_in_db(m_id):
        match_db = TinyDB('database/match.json')
        result = match_db.search(where("m_id") == m_id)   # Search in the database, the match corresponding to the iD provided as input.
        if result:
            return result[0]
        return "no match in db"

    @staticmethod
    def update_match_data( key, value, m_id):
        # db horizontal?
        match_db = TinyDB('database/players.json')
        match = Match.search_match_in_db(p_id)
        # print(match)
        if match:
            return match_db.update({key: value}, where("m_id") == m_id)    
        return "erreur dans les paramètres"

    @staticmethod   # can be called without creating an instance of the class
    def load_all_match_in_db():
        match_db = TinyDB('database/match.json')
        return match_db.all()


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


