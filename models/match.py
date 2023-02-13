from tinydb import TinyDB, Query, where


class Match():

    matches_database = TinyDB("database/matches.json", indent=4)
  
    def __init__(self, match_id, player_1, score_p1, player_2, score_p2):
        self.match_id = str(match_id)
        self.match = ([player_1, score_p1], [player_2, score_p2])   # single match stored as a tuple containing two lists

 #-------------------------------------------------------------------------------------------------

    def __str__(self):
        return f"{self.match[0][1]} vs {self.match[1][0]}"

    def __repr__(self):
        return f"Match({self.match[0][1]}, {self.match[1][0]})"

 #------------------------------------------------------------------------------------------------

    def format_match_in_data(self):
        return {"result": self.match}

    def save_match_in_database(self):
            return self.matches_database.insert(self.format_match_in_data())

 #---------------------------------------------------------------------------------------------------
 
    @staticmethod   # can be called without creating an instance of the class
    def find_match_in_database(match_id):
        matches_database = TinyDB('database/matches.json')
        result = matches_database.search(where("match_id") == match_id)   # Search in the database, the match corresponding to the id provided as input.
        if result:
            return result[0]
        return "No match in database"

    @staticmethod
    def update_match_in_database(key, value, match_id):
        matches_database = TinyDB('database/matches.json')
        match = Match.find_match_in_database(match_id)
        if match:
            return matches_database.update({key:value}, where("match_id") == match_id)    
        return "Error in parameters"

    # def update_score(self, new_score1, new_score2):
    #     self.pairs[0][1] = new_score1
    #     self.pairs[1][1] = new_score2 

    @staticmethod
    def load_all_matches_from_db():
        matches_database = TinyDB('database/matches.json')
        return matches_database.all()


from faker import Faker
fake = Faker(locale="fr_FR")
scores = [75, 80, 85, 90, 95, 100]
test_m_id= [0, 1, 2, 3, 4]
for _ in range(10):
    match = Match(
        match_id= fake.random_element(elements=test_m_id),
        player_1 = fake.first_name(),
        player_2 = fake.first_name(), 
        score_p1 = fake.random_element(elements=scores),
        score_p2 = fake.random_element(elements=scores))
   
    # print(match.__str__())
    # print(match.__repr__())
    # print(match.save_match_in_database())
    # print(match.find_match_in_database("1"))
    # print(match.load_all_matches_from_db())
    # print(match.update_match_in_database("score_p1", 80, "0"))
    print("_"*10)


