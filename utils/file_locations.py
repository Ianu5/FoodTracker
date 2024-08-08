import os

# TODO I need to give those file locations callabe and unique variables
# so I can use them in the main application
# TODO I also need to correct the file paths so our application can find the files
# in the folders there are now
# folder name services
directory = os.getcwd()
folder = 'data'
filename = 'en.openfoodfacts.org.products.csv.gz'
filepath = os.path.join(self.directory, self.folder, self.filename)
downloadpath = Path('./food_databank')


filename = "UserDatabank.json"
directory = os.getcwd()
folder = "UserData"
dir_path = os.path.join(directory, folder)
filepath = os.path.join(directory, folder, filename)