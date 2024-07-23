import csv
import os
import gzip
import openfoodfacts
from pathlib import Path
import pandas
import pickle

class FoodCSV:
    """This class's function is to download the CSV file from the openfood
    facts resources and check if the file exists"""
    directory = os.getcwd()
    folder = 'food_databank'
    filename = 'en.openfoodfacts.org.products.csv.gz'
    filepath = os.path.join(directory, folder, filename)
    downloadpath = Path('./food_databank')

    def download_csv():
        if not os.path.exists(FoodCSV.filepath):
            openfoodfacts.ProductDataset(dataset_type='csv',
                                        cache_dir=FoodCSV.downloadpath)

    def __bool__():
        return os.path.exists(FoodCSV.filepath)


class FoodDataframe:
    def __init__(self):
        self.fields = [
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
        self.csv_data = FoodCSV()
        self.directory = os.getcwd()
        self.folder = 'food_databank'
        self.filename = 'food_dataframe.pkl'
        self.filepath = os.path.join(self.directory, self.folder, self.filename)
        if not os.path.exists(self.filepath):
            self.create_dataframe()

    def create_dataframe(self):
        if not self.csv_data:
            self.csv_data.download_csv()
        chunk_size = 100000
        datachunk_list = []
        for chunk in pandas.read_csv(self.csv_data,
                                     low_memory=False,
                                     sep='\t',
                                     compression='gzip',
                                     on_bad_lines='skip',
                                     chunksize=chunk_size,
                                     usecols=self.fields):
            datachunk_list.append(chunk)
        dataframe = pandas.concat(datachunk_list)
        with open(self.filepath, 'wb') as file:
            pickle.dump(dataframe, file, protocol=pickle.HIGHEST_PROTOCOL)
            print("Food Data successfully imported")

    def get_dataframe(self):
        with open(self.filepath, 'rb') as file:
            df_loaded = pickle.load(file)
        return df_loaded

"""           TODO                         
- create another class which returns the pickle file as
a pandas dataframe
- rename the other classes to avoid confusion
- create functions to search for specific foods
    by name
    by code
    etc
"""




"""Obsolete"""
class FoodData:
    """This class handles the csv file from openfoodfacts and returns an
    iterator which shows the data in dictionary format."""
    fields = [
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
    def __init__(self):
        # Specifying the path in which the file is stored
        self.csv_filename = 'en.openfoodfacts.org.products.csv.gz'
        self.pkl_filename = 'food_dataframe.pkl'
        self.directory = os.getcwd()
        self.folder = 'food_databank'
        self.csv_filepath = os.path.join(self.directory,
                                     self.folder,
                                     self.csv_filename)
        self.pkl_filepath = os.path.join(self.directory,
                                         self.folder,
                                         self.pkl_filename)
        self.fields = FoodData.fields

        # If the csv file does not exist download it into the food_databank folder
        # Using openfoodfacts python sdk for downloading the file
        self.download_path = Path('./food_databank')
        if not os.path.exists(self.csv_filepath):
            self.dataset = openfoodfacts.ProductDataset(dataset_type='csv',
                                                    cache_dir=self.download_path)
        
        chunksize = 100000
        df_frame_list = []
        if not os.path.exists(self.pkl_filepath):
            for chunk in pandas.read_csv(self.csv_filepath,
                                         low_memory=False,
                                         sep='\t',
                                         compression='gzip',
                                         on_bad_lines='skip',
                                         chunksize=chunksize,
                                         usecols=self.fields):
                df_frame_list.append(chunk)
            df_complete = pandas.concat(df_frame_list)
            with open(self.pkl_filepath, 'wb') as file:
                pickle.dump(df_complete, file, protocol=pickle.HIGHEST_PROTOCOL)
                print("Successfully converted to pandas")
            
    """                             TODO                                     """    
    """I will need to write the functions of this class newly as I decided to
    convert the csv to a pandas dataframe so we can work with it easier.
    iter and search food functions need to be written new maybe I will need to 
    redefine the logic of this class so it better represents the data type we work
    with here"""
    def __iter__(self):
        """
        Method to return an iterator for the items in the dataset
        """
        with gzip.open(self.filepath, mode='rt', encoding='utf-8', newline='') as file:
            reader = csv.DictReader(file, delimiter='\t')
            for row in reader:
                yield(dict(row))

    def search_food(self, item: str, parameter): #TODO how do I store the result of the search in what format do I return the shit
        # The type is for setting by which parameter we are going to search the databank by
        for product in self:
            if product[parameter] == item:
                for i in range(len(self.fields)):
                    if product[self.fields[i]]: # TODO I will have to change the print statement to something so I can return this information
                        print(f'{self.fields[i]}: {product[self.fields[i]]}')

    def dataframe(self):
        with open(self.pkl_filepath, 'rb') as file:
            df_loaded = pickle.load(file)
        return df_loaded
