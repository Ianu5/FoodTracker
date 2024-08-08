class Menu:
    def __init__(self, title, options: list):
        self.title = title
        self.options = options
        self.exit_option = len(options) + 1
        
    def display(self):
        print(f"\n{self.title}")
        for idx, option in enumerate(self.options, 1):
            print(f"{idx}. {option['description']}")
        print(f"{self.exit_option}. Exit")

    def get_choice(self):
        while True:
            try:
                choice = int(input("Choose: "))
                if 1 <= choice <= self.exit_option:
                    return choice
                else:
                    print("Invalid choice.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def execute_choice(self, choice):
        if choice == self.exit_option:
            print("Exiting ...")
            return False
        else:
            action = self.options[choice - 1]['action']
            if isinstance(action, Menu):
                action.run()
            else:
                action()
            return True

    def run(self):
        while True:
            self.display()
            choice = self.get_choice()
            if not self.execute_choice(choice):
                break

""" These options are saved in utils for use in the main program
main_menu_options = [
    {'description': 'Choose user', 'action': users_menu},
    {'description': 'Add user', 'action': add_user},
    {'description': 'Delete user', 'action': delete_user}
    ]

calorie_app_menu_options = [
    {'description': 'Search food', 'action': search_food},
    {'description': 'Track calories', 'action': track_food},
    {'description': 'Display history', 'action': display_history},
    {'description': 'Recipes', 'action': recipe_menu}
    ]
"""