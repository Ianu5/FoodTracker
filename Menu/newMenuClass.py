class Menu:
    def __init__(self, options: dict):
        # Dict in format '1': ('option name', function)
        self.options = options

    def print_menu(self):
        print("\n*****MENU*****\n")
        for num, (description, _) in self.options.items():
            print(num, description)

    def handle_menu_choice(self):
        choice = input("\nMake a selection: ")
        action = self.options.get(choice)

        if action:
            action[1]()
        else:
            print("Invalid option")
