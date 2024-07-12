import csv
import os
import gzip
import openfoodfacts
from pathlib import Path


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
        self.filename = 'en.openfoodfacts.org.products.csv.gz'
        self.directory = os.getcwd()
        self.folder = 'food_databank'
        self.filepath = os.path.join(self.directory,
                                     self.folder,
                                     self.filename)
        self.fields = FoodData.fields

        # If the file does not exist download it into the food_databank folder
        # Using openfoodfacts python sdk for downloading the file
        self.download_path = Path('./food_databank')
        if not os.path.exists(self.filepath):
            self.dataset = openfoodfacts.ProductDataset(dataset_type='csv',
                                                    cache_dir=self.download_path)

    def __iter__(self):
        """
        Method to return an iterator for the items in the dataset
        """
        with gzip.open(self.filepath, mode='rt', encoding='utf-8', newline='') as file:
            reader = csv.DictReader(file, delimiter='\t')
            for row in reader:
                yield(dict(row))

    def search_food(self, name: str, type): #TODO how do I store the result of the search in what format do I return the shit
        # The type is for setting by which parameter we are going to search the databank by
        for product in self:
            if product['product_name'] == name:
                for i in range(len(self.fields)):
                    if product[self.fields[i]]: # TODO I will have to change the print statement to something so I can return this information
                        print(f'{self.fields[i]}: {product[self.fields[i]]}')
