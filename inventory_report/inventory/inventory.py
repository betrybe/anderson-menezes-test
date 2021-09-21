from inventory_report.importer.importer import Importer
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory():
    @staticmethod
    def import_data(file: str, report_type: str) -> str:
        if Importer.get_file_extension(file) == '.csv':
            return Inventory.generate_report_from_file(file, report_type,
                                                       CsvImporter())
        elif Importer.get_file_extension(file) == '.xml':
            return Inventory.generate_report_from_file(file, report_type,
                                                       XmlImporter())
        elif Importer.get_file_extension(file) == '.json':
            return Inventory.generate_report_from_file(file, report_type,
                                                       JsonImporter())
        else:
            raise ValueError('Wrong file type.')

    @staticmethod
    def generate_report_from_file(file: str, report_type: str,
                                  data_importer: Importer) -> str:
        if report_type == 'simples':
            return SimpleReport.generate(data_importer.import_data(file))
        elif report_type == 'completo':
            return CompleteReport.generate(data_importer.import_data(file))
        else:
            raise ValueError('Wrong report type.')
