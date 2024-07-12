import UserDatabankClass
import FoodDataBankClass
from MenuClass import *

def main():
    food_databank = FoodDataBankClass.FoodData()
    user_databank = UserDatabankClass.UserDatabank()
    menu = EntryMenu()
    while True:
        menu.display()
        menu.set_choice()
        menu.handle_choice(user_databank)

if __name__ == "__main__":
    main()