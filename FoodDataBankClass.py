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


class FoodData:
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
