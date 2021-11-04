"""
File: abstract_bag.py
Author: Ken Lambert
"""
from abc import ABC, abstractmethod
class AbstractBag(ABC):
    """An abstract bag implementation."""

    # Constructor
    @abstractmethod
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self.size = 0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    # Accessor methods
    def isEmpty(self):
        """Returns True if len(self) == 0, or False otherwise."""
        return len(self) == 0
    
    def __len__(self):
        """Returns the number of items in self."""
        return self.size

    def __str__(self):
        """Returns the string representation of self."""
        return "{" + ", ".join(map(str, self)) + "}"

    def __add__(self, other):
        """Returns a new bag containing the contents
        of self and other."""
        result = type(self)(self)
        for item in other:
            result.add(item)
        return result

    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        if self is other: return True
        if type(self) != type(other) or \
           len(self) != len(other):
            return False
        for item in self:
            if self.count(item) != other.count(item):
                return False
        return True

    def count(self, item):
        """Returns the number of instances of item in self."""
        total = 0
        for nextItem in self:
            if nextItem == item:
                total += 1
        return total

    @abstractmethod
    def __contains__(self, item: object) -> bool:
        """Overrides the in operator to see if an item is in the collection.

        Args:
            item (object): Item to compare.

        Returns:
            bool: True if item is in the collection, False if not.
        """
        return False

    @abstractmethod
    def __iter__(self):
        """Supports iteration over a view of self."""
        return None

    @abstractmethod
    def add(self, item):
        """Adds item to self."""
        pass

    @abstractmethod
    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item in not in self.
        Postcondition: item is removed from self."""
        pass