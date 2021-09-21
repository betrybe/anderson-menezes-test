import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.importer import Importer
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.importer.json_importer import JsonImporter


def main():
    arg_count = len(sys.argv)
    if(arg_count < 3):
        print('Verifique os argumentos', file=sys.stderr)
    else:
        file_path = sys.argv[1]
        report_type = sys.argv[2]
        file_extension = Importer.get_file_extension(file_path)
        if file_extension == '.csv':
            inventory = InventoryRefactor(CsvImporter())
            print(inventory.import_data(file_path, report_type), end='')
        elif file_extension == '.xml':
            inventory = InventoryRefactor(XmlImporter())
            print(inventory.import_data(file_path, report_type), end='')
        elif file_extension == '.json':
            inventory = InventoryRefactor(JsonImporter())
            print(inventory.import_data(file_path, report_type), end='')
        else:
            raise ValueError('Arquivo inválido')


if __name__ == '__main__':
    main()
