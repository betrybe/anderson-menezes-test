import pathlib
from abc import ABC, abstractmethod
from typing import List


class Importer(ABC):

    @abstractmethod
    def import_data(file_name: str) -> List:
        ...

    @abstractmethod
    def get_inventory_list_from_file(file_name: str) -> List:
        ...

    @staticmethod
    def is_correct_file_extension(file_name: str,
                                  extension: str) -> bool:
        file_extension = Importer.get_file_extension(file_name)
        if file_extension != extension:
            return False
        return True

    @staticmethod
    def get_file_extension(file_name: str) -> str:
        return pathlib.Path(file_name).suffix
