import sys
import json
from inventory_report.importer.importer import Importer
from inventory_report.exceptions.extension_exception import ExtensionException


class JsonImporter(Importer):

    def import_data(self, file_name):
        if not self.is_correct_file_extension(file_name, '.json'):
            raise ExtensionException('.json')
        inventory_data = self.get_inventory_list_from_file(file_name)
        return inventory_data

    def get_inventory_list_from_file(self, file_name):
        try:
            with open(file_name) as f:
                inventory_data = json.loads(f.read())
            return inventory_data
        except Exception as e:
            print('Problems processing file: ' + repr(e))
            sys.exit()
