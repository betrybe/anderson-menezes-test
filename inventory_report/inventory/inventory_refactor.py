from collections.abc import Iterable
from typing import List
from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.importer.importer import Importer
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class InventoryRefactor(Iterable):

    _data: List = None

    def __init__(self, importer: Importer) -> None:
        self._importer = importer

    def __iter__(self) -> InventoryIterator:
        return InventoryIterator(self._data)

    def import_data(self, file: str, report_type: str) -> str:
        self._data.append(self._importer.import_data(file))
        if report_type == 'simples':
            return SimpleReport.generate(self._data)
        elif report_type == 'completo':
            return CompleteReport.generate(self._data)
        else:
            raise ValueError('Wrong report type.')
