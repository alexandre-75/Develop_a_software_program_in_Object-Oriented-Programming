class PlayerView():

    def __init__(self):
        pass

    def summary_of_new_player_created(self, info):
        """
        Display a summary of a newly created player.
        Args:
            info (dict): A dictionary containing the player's information.
        """

        print("---------- summary of new player created ----------")
        print(f"first name : {info['first_name']}")
        print(f"Last name : {info['last_name']}")
        print(f"Date of birth : {info['date_of_birth']}")
        print(f"Player ID : {info['player_id']}")
        print(f"Score of player: {info['score_of_player']}")
        print(f"Rank : {info['ranking']}")

    def player_message_is_saved_in_the_database(self):

        """
        Display a message indicating that the player information was saved in the database.
        """

        print("player information is correctly saved in the database")

    def player_message_not_saved_in_the_database(self):

        """
        Display a message indicating that the player information was not saved in the database.
        """

        print("player information is not saved in the database")

    def display_available_players(self, players):

        """
        Display a list of available players.

        Args:
            players (list): A list of dictionaries containing player information.
        """

        print("id, Last Name, First Name")
        for i, player in enumerate(players):
            print(f"{i+1} - {player['last_name']} {player['first_name']} (id: {player['player_id']})")

    def display_player_update_options(self, options):

        """
        Display a list of options for updating a player's information.

        Args:
            options (list): A list of strings representing the options for updating a player's information.
        """

        for i, option in enumerate(options):
            print(f"[{i+1}] Update {option}")

    def exit_save_player(self):

        """
        Display a message indicating how to stop saving a player's information.
        """

        print("write [quit] to stop saving")

    def exit_player_creation_or_continue(self):

        """
        Display a message asking whether to exit player creation or continue.

        The message also indicates how to exit player creation without saving.
        """

        print("enter the player_id at least")
        print("press [b] to exit without creating a player otherwise press [a] to continue")

    def non_editable_value(self):

        """
        Display a message indicating that a value cannot be changed.
        """

        print("this value cannot be changed")
