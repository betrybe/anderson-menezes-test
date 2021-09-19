import pathlib
from abc import ABC, abstractmethod


class Importer(ABC):

    @abstractmethod
    def import_data(self, file_name):
        ...

    @abstractmethod
    def get_inventory_list_from_file(self, file_name):
        ...

    def is_correct_file_extension(self, file_name, extension):
        file_extension = self.get_file_extension(file_name)
        if file_extension != extension:
            return False
        return True

    def get_file_extension(self, file_name):
        return pathlib.Path(file_name).suffix
