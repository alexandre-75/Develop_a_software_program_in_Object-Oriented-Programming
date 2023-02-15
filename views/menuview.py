class MainMenu():

    def __init__(self):
        pass

    @staticmethod   
    def display_main_menu():
        return print("""Menu      
                1. Start a Tournament
                2. Add a new player to the database
                3. update a player from the database
                4. EXIT""")

    @staticmethod
    def exit_the_program():
        print("exit the program ? [yes/no] ")

    @staticmethod
    def input_a_number():
        return int(input("Enter a number : "))
     
    @staticmethod
    def input_prompt():
        print("Enter a: ")
    
    @staticmethod
    def input_prompt_text_2(option):
        print(f"\nEnter {option}: ")
    
    @staticmethod
    def input_prompt_text(prompt):
        return input(prompt)