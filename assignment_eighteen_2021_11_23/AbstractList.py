from abc import ABC, abstractmethod
from typing import Iterator


class AbstractList(ABC):
    def __init__(self, sourceCollection = None) -> None:
        self.modCount = 0
        self.size = 0

        if sourceCollection:
            for x in sourceCollection:
                self.add(x)
    
    def getModCount(self) -> int:
        return self.modCount

    def incModCount(self) -> None:
        self.modCount += 1

    def index(self, item: object) -> int:
        """Returns the index of an item.

        Args:
            item (object): The item to find an index of.

        Returns:
            int: The index of the first instance of the item
            in the list.

        Raises:
            ValueError: When the item is not in the list.
        """
        pos = 0
        for data in self:
            if data == item:
                return pos
            else:
                pos += 1
        raise ValueError(str(item) + " not in list.")

    def add(self, item: object) -> None:
        self.insert(len(self), item)

    def remove(self, item: object) -> None:
        pos = self.index(item)
        self.pop(pos, item)

    def isEmpty(self) -> bool:
        return self.size() == 0

    def size(self) -> int:
        return self.size



    def __str__(self) -> str:
        val = list(map(str, self))
        return "{" + ', '.join(val) + "}"

    def __eq__(self, o: object) -> bool:
        if type(self) != type(o): return False
        if self.size() != o.count(): return False
        it = iter(o)
        for x in self:
            if x != next(it):
                return False

        return True


    # Abstract Methods


    @abstractmethod
    def insert(self, index: int, item: object) -> None:
        pass

    @abstractmethod
    def pop(self, index: int) -> None:
        pass

    @abstractmethod
    def clear(self) -> None:
        """Clears the list of all values.
        """
        pass

    @abstractmethod
    def listIterator(self):
        """Creates a new List Iterator for this List.
        """
        pass

    

    @abstractmethod
    def __len__(self) -> int:
        """Returns the physical length of the list.

        Returns:
            int: The physical length of the list.
        """
        pass

    @abstractmethod
    def __iter__(self) -> Iterator:
        """Returns the iterator for this list.

        Yields:
            Iterator: The iterator for this list.
        """
        pass
    
    @abstractmethod
    def __getitem__(self, i: int) -> object:
        """Get an item from the list at an index.

        Args:
            i (int): Index to get an item from.

        Returns:
            object: The object at the selected position

        Raises:
            IndexError: When the index is out of range of the
            list.
        """
        pass

    @abstractmethod
    def __setitem__(self, i:int, o: object) -> None:
        
        """Sets an item at a specific index of the list.

        Args:
            i (int): Index to set an item at.
            o (object): The object to set at the provided index.

        Raises:
            IndexError: When the index is out of range of the
            list.
        """
        pass

