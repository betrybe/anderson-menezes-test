import pathlib
from abc import ABC, abstractmethod
from typing import List


class Importer(ABC):

    @abstractmethod
    def import_data(self, file_name: str) -> List:
        ...

    @abstractmethod
    def get_inventory_list_from_file(self, file_name: str) -> List:
        ...

    def is_correct_file_extension(self, file_name: str,
                                  extension: str) -> bool:
        file_extension = self.get_file_extension(file_name)
        if file_extension != extension:
            return False
        return True

    @staticmethod
    def get_file_extension(file_name: str) -> str:
        return pathlib.Path(file_name).suffix
