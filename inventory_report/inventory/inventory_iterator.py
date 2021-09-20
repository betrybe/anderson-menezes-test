from collections.abc import Iterator
from inventory_report.inventory.inventory_refactor import InventoryRefactor


class InventoryIterator(Iterator):
    _position: int = None

    def __init__(self, collection: InventoryRefactor) -> None:
        self._collection = collection
        self._position = 0

    def __next__(self):
        try:
            value = self._collection[self._position]
            self._position += 1
        except IndexError:
            raise StopIteration()

        return value
