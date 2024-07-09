import UserDatabankClass
import CSVHandler
from MenuClass import *

def main():
    food_databank = CSVHandler.CSVHandler()
    user_databank = UserDatabankClass.UserDatabank()
    menu = EntryMenu()
    while True:
        menu.display()
        menu.set_choice()
        menu.handle_choice(user_databank)

if __name__ == "__main__":
    main()