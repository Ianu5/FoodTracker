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
    folder = "UserData"
    dir_path = os.path.join(directory, folder)
    filepath = os.path.join(directory, folder, filename)

    def __init__(self):
        self.filepath = UserDatabank.filepath

        # check if the file exists and initialize the datastructure
        if (os.path.exists(self.filepath)
            and os.path.isfile(self.filepath)
            and self.filepath.endswith(".json")):
            with open(self.filepath, 'r') as f:
                self.data = json.load(f)
        else:
            os.makedirs(self.dir_path)
            self.data = {}

    def prompt_user_information(self):
        # List with the information needed
        required_information = (
            'first_name',
            'last_name',
            'age',
            'height',
            'weight',
            'gender',
            'pal'
            )
    
        # Prompting the user for each element in the tuple and putting it 
        # in a dictionary
        user = {
                element: input(f'{element.replace('_', ' ')}: ') 
                    for element in required_information
                }
        return user

    def add_user(self):
        # Prompting the user for a username
        username = input("Choose username: ")

        # Check if the username already exists
        if username in self.data.keys():
            print("Username taken choose another")
            self.add_user()
            return None

        # Get all required data            
        self.data[username] = self.prompt_user_information()

        # Save the data to our json file
        json_string = json.dumps(self.data, indent=4)
        with open(self.filepath, 'w') as f:
            f.write(json_string)
        return None

    def delete_user(self):
        # showing which users exist
        self.show_users()
        username = input("Input the username you want to delete: ")
        # Check if the username exist in our Databank
        # and delete it if we find it
        if username in self.data.keys():
            del self.data[username]
            print("Successfully deleted the user")
        
       # Saving the changes in the file 
        json_string = json.dumps(self.data, indent=4)
        with open(self.filepath, 'w') as f:
            f.write(json_string)

    def display_user_information(self, username):
        # Function to display all the information about one user
        if username in self.data.keys():
            user_information = {key: value for key, value in self.data[username].items()}
        print(user_information)
        return None

    def show_users(self):
        # Printing all users that exist in our databank
        users = [user for user in self.data.keys()]
        for num, user in enumerate(users, start=1):
            print(num, user)
        return None
    
    def return_users(self):
        return [user for user in self.data.keys()]