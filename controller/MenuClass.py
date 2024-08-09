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
        self.display()
        choice = self.get_choice()
        return self.execute_choice(choice)
            

class ChooseUserMenu(Menu):
    def __init__(self, title, options: list, user):
        super().__init__(title, options)
        self.user = user
    
