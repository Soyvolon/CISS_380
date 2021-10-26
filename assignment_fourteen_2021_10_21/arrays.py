"""
File: arrays.py

An Array is a restricted list whose clients can use
only [], len, iter, and str.

To instantiate, use

<variable> = array(<capacity>, <optional fill value>)

The fill value is None by default.
"""

class Array(object):
    """Represents an array."""

    def __init__(self, capacity, fillValue = None):
        """Capacity is the static size of the array.
        fillValue is placed at each position."""
        self.__logical_size = 0
        self.__fill = fillValue
        self.__dcap = capacity

        self.items = list()
        for count in range(capacity):
            self.items.append(self.__fill)

    def __len__(self):
        """-> The capacity of the array."""
        return len(self.items)

    def __str__(self):
        """-> The string representation of the array."""
        return str(self.items)

    def __iter__(self):
        """Supports iteration over a view of an array."""
        for i in range(0, self.size()):
            yield self.items[i]

    def __getitem__(self, index):
        """Subscript operator for access at index."""
        if index >= 0 and index < self.size():
            return self.items[index]
        else:
            raise IndexError("Index eout of range of Array.")

    def __setitem__(self, index, newItem):
        """Subscript operator for replacement at index."""
        if index >= 0 and index < self.size():       
            self.items[index] = newItem
        else:
            raise IndexError("Index out of range of Array.")

    def __eq__(self, o: object) -> bool:
        if type(self) != type(o):
            return False
        
        sLs = self.size()
        oLs = o.size()
        if sLs != oLs:
            return False

        for i in range(0, sLs):
            if self[i] != o[i]:
                return False

        return True

    def __contains__(self, item):
        return item in self.items

    def _grow(self):
        ls = self.size()
        ps = len(self)
        if ls == ps:
            tmp = [self.__fill for i in range(ps * 2)]
            if len(tmp) == 0:
                tmp = [self.__fill]
            for i in range(0, ls):
                tmp[i] = self.items[i]
            self.items = tmp

    def _shrink(self):
        ls = self.size()
        ps = len(self)
        if ps // 4 > ls and ps >= self.__dcap * 2:
            tmp = [self.__fill for i in range(ps // 2)]
            for i in range(0, ls):
                tmp[i] = self[i]
            self.items = tmp

    def insert(self, index, item):
        if index < 0:
            raise IndexError("Insert index must be above or equal to 0.")

        ls =  self.size()
        if index > ls:
            index = ls
        self._grow()
        if ls > 0:
            for i in range(ls, index - 1, -1):
                self.items[i] = self.items[i - 1]
        self.items[index] = item
        self.__logical_size += 1

    def pop(self, index):
        lsm = self.size() - 1
        if index < 0 or index > lsm:
            raise IndexError("Index out of range of array.")
        self._shrink()

        item = None
        if lsm != index:
            for i in range(index, lsm):
                if i == index:
                    item = self.items[i]
                self.items[i] = self.items[i + 1]
        else:
            item = self.items[index]

        self.items[lsm] = self.__fill
        self.__logical_size -= 1

        return item

    def default(self):
        return self.__fill

    def size(self):
        return self.__logical_size