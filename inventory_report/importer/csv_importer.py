import sys
import csv
from typing import List
from inventory_report.exceptions.extension_exception import ExtensionException
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):

    def import_data(self, file_name: str) -> List:
        if not self.is_correct_file_extension(file_name, '.csv'):
            raise ExtensionException('.csv')
        inventory_data = self.get_inventory_list_from_file(file_name)
        return inventory_data

    def get_inventory_list_from_file(self, file_name: str) -> List:
        try:
            with open(file_name) as f:
                inventory_data = [{k: v for k, v in row.items()}
                                  for row in csv.DictReader(f,
                                  skipinitialspace=True)]
            return inventory_data
        except Exception as e:
            print('Problems processing file: ' + repr(e))
            sys.exit()
