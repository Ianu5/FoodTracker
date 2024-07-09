from UserDatabankClass import *
import sys


class Menu:
    def __init__(self, *options):
        self.options = options
        self.choice = None

    def display(self):
        for index, item in enumerate(self.options, start=1):
            print(index, item)
        print()
        return None

    def set_choice(self):
        self.choice = input("Choice: ")
        if int(self.choice) not in range(len(self.options) + 1):
            print("Not a valid option")
            self.set_choice()
            return None
        return None


class EntryMenu(Menu):
    options = ("Choose user", "Add user", "Delete user", "Exit")
    def __init__(self):
        self.options = EntryMenu.options

    def display(self):
        return super().display()
    
    def set_choice(self):
        return super().set_choice()
        
    def handle_choice(self, userdatabank: UserDatabank):
        match self.choice:
            case '1':
                userdatabank.show_users()
                users = userdatabank.return_users()
                choice = int(input("Choose: "))
                if 1 <= choice <= len(users):
                    print(users[choice - 1])
            case '2':
                userdatabank.add_user()
            case '3':
                userdatabank.delete_user()
            case '4':
                sys.exit("Exiting the program")


class UserMenu(Menu):
    options = ("Search food", "Enter food eaten", "Display eating history", "Add recipie")
    def __init__(self):
        self.options = UserMenu.options()

    def display(self):
        return super().display()
    
    def set_choice(self):
        return super().set_choice()
