import csv
import os
import gzip


# TODO I will need to write the code for downloading the csv file automatically
# and placing it in the right folder for usage
class CSVHandler:
    def __init__(
            self
    ):
        """
        This class handles the csv file from openfoodfacts and returns an
        iterator which shows the data in dictionary format.
        """
        self.filename = 'en.openfoodfacts.org.products.csv.gz'
        self.directory = os.getcwd()
        self.folder = 'food_databank'
        self.filepath = os.path.join(self.directory, self.folder, self.filename)

    def __iter__(self):
        with gzip.open(self.filepath, mode='rt', encoding='utf-8', newline='') as file:
            reader = csv.DictReader(file, delimiter='\t')
            for row in reader:
                yield(dict(row))
