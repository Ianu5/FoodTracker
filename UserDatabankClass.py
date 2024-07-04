import os
import json

class User:
    def __init__(self, username: str,  first_name: str, last_name: str, age: int,
                 height: float, weight: float, gender: str,
                 physical_activity_level: float):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.age = int(age)
        self.height = float(height)
        self.weight = float(weight)
        self.gender = gender if gender in ['m', 'f'] else None
        self.physical_activity_level = float(physical_activity_level)
        self.basal_rate = User.get_basal_rate(self.gender, self.weight, self.height, self.age)
        self.performance_rate = User.get_performance_rate(self.basal_rate, self.physical_activity_level)

    @staticmethod
    def get_basal_rate(gender, weight, height, age):
        if gender == 'f':
            return int(447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age))
        elif gender == 'm':
            return int(88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age))

    @staticmethod
    def get_performance_rate(basal_rate, PAL):
        return int(basal_rate * PAL)


class UserDatabank:
    """
    This class initiates a json file for the storage of the user
    information in the databank it comes with methods to add users
    and makes use of the User class
    """
    # Set the name and filepath of the Databank
    filename = "UserDatabank.json"
    directory = os.getcwd()
    folder = 'UserData'
    filepath = os.path.join(directory, filename)

    def __init__(self):
        self.filepath = UserDatabank.filepath

        if (os.path.exists(self.filepath)
            and os.path.isfile(self.filepath)
            and self.filepath.endswith(".json")):
            with open(self.filepath, 'r') as f:
                self.data = json.load(f)
        else:
            self.data = []

    def get_user_information(self, username):
        required_information = (
            'first_name',
            'last_name',
            'age',
            'height',
            'weight',
            'gender',
            'pal'
            )
    
        user = {
            username: {
                element: input(f'{element.replace('_', ' ')}: ') 
                    for element in required_information
                }
        }

        return user

    def add_user(self):
        username = input("Choose username: ")

        if username in self.data:
            print("Username taken choose another")
            self.add_user()
            
        new_user = self.get_user_information(username)
        self.data.append(new_user)
        json_string = json.dumps(self.data, indent=4)

        with open(self.filepath, 'w') as f:
            f.write(json_string)
        return None

    def __contains__(self, username):
        return next((element for element in self.data 
                    if username in element.keys()), None)
        #return user
    
    #def __contains__(self, username):
    #    return username in self.data.keys()