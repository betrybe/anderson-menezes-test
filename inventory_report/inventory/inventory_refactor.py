from collections.abc import Iterable
from inventory_report.importer.importer import Importer
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.inventory.inventory_iterator import InventoryIterator


class InventoryRefactor(Iterable):

    def __init__(self, importer: Importer) -> None:
        self.importer = importer
        self.data = []

    def __iter__(self) -> InventoryIterator:
        return InventoryIterator(self.data)

    def import_data(self, file: str, report_type: str) -> str:
        self.data.extend(self.importer.import_data(file))
        if report_type == 'simples':
            return SimpleReport.generate(self.data)
        elif report_type == 'completo':
            return CompleteReport.generate(self.data)
        else:
            raise ValueError('Wrong report type.')
