class TournamentView():

    def __init__(self):
        pass

    def summary_of_new_tournament_created(self, info, players):

        """
        Print a summary of a new tournament that has been created.
        
        Args:
            info (dict): A dictionary containing information about the new tournament.
            players (list): A list of players in the tournament.
        """

        print(f"{info['tournament_id']}, {info['tournament_name']}")
        print(f"site: {info['tournament_site']}")
        print(f"Rounds: {info['current_round']}/{info['number_of_rounds']}")
        print(f"general_remarks: {info['general_remarks']}")

        for i in players:
            print(f"Player {players.index(i) + 1}:")
            print(f"{i['player_id']}")
            print(f"{i['last_name']}, {i['first_name']}")
            print(f"{i['date_of_birth']}")

    def tournament_message_is_saved_in_the_database(self):

        """
        Print a message indicating that tournament information has been saved in the database.
        """

        print("tournament information is correctly saved")

    def message_start_tournament(self):

        """
        Print a message asking if the user wants to start the tournament.
        """

        print("Start tournament now ? [yes/no] ")

    def invalid_player_id(self):

        """
        Print a message indicating that the player ID is not recognized.
        """

        print("the identifier is not recognized, try again")

    def select_tournament(self, tournaments_list):

        """
        Print a table of all tournaments in a list.
        
        Args:
            tournaments_list (list): A list of dictionaries containing information about tournaments.
        """

        if len(tournaments_list) == 0:
            print("No tournaments found.")
        else:
            print("{:<5} {:<20} {:<20} {:<30} {:<15} {:<15} {:<10}".format(
                "ID", "Name", "Location", "Description", "Start Date", "End Date", "Current Round"
            ))
            for tournament in tournaments_list:
                print("{:<5} {:<20} {:<20} {:<30} {:<15} {:<15} {:<10}".format(
                    tournament['tournament_id'],
                    tournament['tournament_name'],
                    tournament['tournament_site'],
                    tournament['start_date'],
                    tournament['end_date'],
                    tournament['general_remarks'],
                    f"Round {tournament['current_round']}/{tournament['number_of_rounds']}"
                ))

    def print_error_load_tournament(self):

        """
        Print an error message indicating that there was an error loading a tournament.
        """

        print("an error while loading, enter a valid id")

    def exit_tournament_creation_or_continue(self):

        """
        Print a message asking the user if they want to exit tournament creation or continue.
        """

        print("enter the tournament_id at least")
        print("press [b] to exit without creating a tournmanent otherwise press [a] to continue")
