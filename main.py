from controller.MenuClass import Menu
from services.UserDataBankClass import *

Users = UserDatabank()
main_menu_options = [
    # TODO I need to devise some solution for the Menu where the user chooses a user from the list of possible users
    {'description': 'Choose user', 'action': Menu("User Menu", Users.return_users())},
    {'description': 'Add user', 'action': Users.add_user},
    {'description': 'Delete user', 'action': Users.delete_user}
    ]

"""
calorie_app_menu_options = [
    {'description': 'Search food', 'action': search_food},
    {'description': 'Track calories', 'action': track_food},
    {'description': 'Display history', 'action': display_history},
    {'description': 'Recipes', 'action': recipe_menu}
    ]
"""

def main():
    main_menu = Menu("Main Menu", main_menu_options)
    main_menu.run()

if __name__ == "__main__":
    main()