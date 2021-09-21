import sys
import xml.etree.ElementTree as ET
from typing import List
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):

    @staticmethod
    def import_data(file_name: str) -> List:
        if not XmlImporter.is_correct_file_extension(file_name, '.xml'):
            raise ValueError('Arquivo inválido')
        inventory_data = XmlImporter.get_inventory_list_from_file(file_name)
        return inventory_data

    @staticmethod
    def get_inventory_list_from_file(file_name: str) -> List:
        try:
            tree = ET.parse(file_name)
            root = tree.getroot()

            inventory_data = []

            for item in root.findall('./record'):
                record = {}
                for child in item:
                    record[child.tag] = child.text
                inventory_data.append(record)

            return inventory_data
        except Exception as e:
            print('Problems processing file: ' + repr(e))
            sys.exit()
