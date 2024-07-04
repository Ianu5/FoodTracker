import csv
import os
import gzip
import openfoodfacts
from pathlib import Path


class CSVHandler:
    def __init__(self):
        """
        This class handles the csv file from openfoodfacts and returns an
        iterator which shows the data in dictionary format.
        """

        # Specifying the path in which the file is stored
        self.filename = 'en.openfoodfacts.org.products.csv.gz'
        self.directory = os.getcwd()
        self.folder = 'food_databank'
        self.filepath = os.path.join(self.directory,
                                     self.folder,
                                     self.filename)

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
