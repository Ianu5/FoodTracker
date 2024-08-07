from UserDatabankClass import *
import sys
import openfoodfacts
import FoodDataBankClass

FOOD_DATA = FoodDataBankClass.FoodData()

class Menu:
    """Base Menu class for usage in more elaborate menus"""
    def __init__(self, *options):
        self.options = options
        self.choice = None

    def display(self):
        # Method to display all the options in the menu
        for index, item in enumerate(self.options, start=1):
            print(index, item)
        print()
        return None

    def set_choice(self):
        # method to setting the choice the user inputs as a instance variable
        self.choice = input("Choice: ")
        if int(self.choice) not in range(len(self.options) + 1):
            print("Not a valid option")
            self.set_choice()
            return None
        return None


class EntryMenu(Menu):
    """This class inherits from the menu class and is the first menu the 
    user sees and interacts with. It handles the Users as in choosing,
    adding and deleting users from the Userdatabank"""

    # Options the menu can give the user
    options = ("Choose user", "Add user", "Delete user", "Exit")
    def __init__(self):
        self.options = EntryMenu.options

    def display(self):
        # Inherits the display method from the Menu class this renders
        # the available options for the user
        return super().display()
    
    def set_choice(self):
        # Sets the choice from the user as an instance attribute
        return super().set_choice()
        
    def handle_choice(self, userdatabank: UserDatabank):
        # Acting on the choice of the user
        # initializing an instance of our user databank
        users = userdatabank.return_users()

        # Using match case to handle the input of the user
        match self.choice:
            case '1':
                # In case the user chooses his account he will be forwarded
                # to the Usermenu
                userdatabank.show_users()
                if len(users) != 0:
                    choice = int(input("Choose: "))
                    if 1 <= choice <= len(users):
                        user = users[choice - 1]
                        print(f"\nHello {user} what do you want to do?\n")
                        menu = UserMenu(user)
                        menu.display()
                        menu.set_choice()
                        menu.handle_choice()

            case '2':
                userdatabank.add_user()
            case '3':
                if len(users) != 0:
                    userdatabank.delete_user()
            case '4':
                sys.exit("Exiting the program")
        return None


class UserMenu(Menu):
    options = ("Search food", "Enter food eaten", "Display eating history", "Add recipie", 'Exit')
    def __init__(self, user):
        self.options = UserMenu.options
        self.user = user

    def display(self):
        return super().display()
    
    def set_choice(self):
        return super().set_choice()

    def handle_choice(self):
        match self.choice:
            case '1':
                search_by_choices = FOOD_DATA.fields[0:5:2]
                print("Search by:\n")
                for num, choice in enumerate(search_by_choices, start=1):
                    print(num, choice)
                choice = input("Please enter a selection: ")
                match choice:
                    case '1':
                        FOOD_DATA.search_food(input(f"Enter your {search_by_choices[int(choice) - 1]}: "), search_by_choices[int(choice) - 1])
                # TODO write a class for food info handling
            case '2':
                # TODO write a class for tracking eaten calories
                ...
            case '3':
                # TODO method in calorie tracker that displays the data
                ...
            case '4':
                # TODO refer to the Cookbook class here
                ...