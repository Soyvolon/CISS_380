from bag_interface import BagInterface
from arrays import Array

class ArraySet(BagInterface):
    DEFAULT_CAPACITY = 0

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it’s present."""
        self.__data = None
        self.__size = 0
        self.__init_array(sourceCollection)

    def __init_array(self, sourceCollection = None):
        if sourceCollection != None:
            size = len(sourceCollection)
            self.__data = Array(size)

            for x in sourceCollection:
                self.add(x)
        else:
            self.__data = Array(ArraySet.DEFAULT_CAPACITY)

    # Accessor methods
    def isEmpty(self):
        """Returns True if len(self) == 0,
        or False otherwise."""
        return len(self) == 0

    def __len__(self):
        """Returns the number of items in self."""
        return self.__data.size()

    def __str__(self):
        """Returns the string representation of self."""
        return "{ " + ','.join(map(str, self)) + " }"

    def __iter__(self):
        """Supports iteration over a view of self."""
        return iter(self.__data)

    def __contains__(self, item):
        return item in self.__data

    def __add__(self, other):
        """Returns a new bag containing the contents
        of self and other."""
        if not isinstance(other, ArraySet):
            raise TypeError("Cannot add a non Array Set to an Array Set.")

        newSet = ArraySet(self)
        for x in other:
            newSet.add(x)
        return newSet

    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        if not isinstance(other, ArraySet):
            raise TypeError("Cannot compare a non Array Set to an Array Set.")
        
        if len(self) != len(other):
            return False

        # create a test set of items
        # and attempt to add all other itmes
        # into the test set. If all items are the same
        # the resulting size will be equal to the
        # self objects size.
        data = ArraySet(self)
        for x in other:
            data.add(x)
        if len(data) != len(self):
            return False

        return True
        
    def count(self, item):
        """Returns the number of instances of item in self."""
        if item in self:
            return 1
        else:
            return 0

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self.__data = Array(ArraySet.DEFAULT_CAPACITY)

    def add(self, item):
        """Adds item to self."""
        if item not in self:
            self.__data.insert(self.__size, item)

    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item in not in self.
        Postcondition: item is removed from self."""
        for x in range(0, self.__data.size()):
            if self.__data[x] == item:
                self.__data.pop(x)
                return
        raise KeyError("Item not found in Array Set.")