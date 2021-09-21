import sys
import json
from typing import List
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):

    @staticmethod
    def import_data(file_name: str) -> List:
        if not JsonImporter.is_correct_file_extension(file_name, '.json'):
            raise ValueError('Arquivo inválido')
        inventory_data = JsonImporter.get_inventory_list_from_file(file_name)
        return inventory_data

    @staticmethod
    def get_inventory_list_from_file(file_name: str) -> List:
        try:
            with open(file_name) as f:
                inventory_data = json.loads(f.read())
            return inventory_data
        except Exception as e:
            print('Problems processing file: ' + repr(e))
            sys.exit()
