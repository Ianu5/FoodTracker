from controller.MenuClass import Menu
from services.UserDataBankClass import *

USER = None

def main():
    while True:
        users_db = UserDatabank()
        users = users_db.return_users()
        calorie_app_menu_options = [
            {'description': 'Search food', 'action': None},
            {'description': 'Track calories', 'action': None},
            {'description': 'Display history', 'action': None},
            {'description': 'Recipes', 'action': None}
            ]
        main_menu_options = [
            # TODO I want to devise a function for the choose user option that renders runs the next menu and saves the choice of the user 
            # Or I could move the add and delete user functionality in the Usermenu when the user already chose a user. When the user is not found ask if he wants to add the user
            {'description': 'Choose user', 'action': Menu("Choose user", [{'description': user, 'action': Menu(f"{USER} Calorie Tracker", calorie_app_menu_options)} for user in users])},
            {'description': 'Add user', 'action': users_db.add_user},
            {'description': 'Delete user', 'action': users_db.delete_user}
            ]
        main_menu = Menu("Main Menu", main_menu_options)
        if not main_menu.run():
            break

if __name__ == "__main__":
    main()