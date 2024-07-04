import UserDatabankClass
import CSVHandler

FIELDS = [
    'code',
    'url',
    'product_name',
    'abbreviated_product_name',
    'generic_name',
    'quantity',
    'brands',
    'energy-kj_100g',
    'energy-kcal_100g',
    'energy_100g',
    'unsaturated-fat_100g',
    'carbohydrates_100g',
    'sugars_100g',
    ]

def main():
    userdb = UserDatabankClass.UserDatabank()
    username = input('Your username: ')

    if not username in userdb:
        userdb.add_user()

    print(username in userdb)

if __name__ == "__main__":
    main()