from LinkedListIterator import LinkedListIterator
from AbstractList import AbstractList
from node import TwoWayNode

class LinkedList(AbstractList):
    
    def __init__(self, sourceCollection = None):
        self.head : TwoWayNode = TwoWayNode()
        self.head.previous = self.head.next = self.head

        AbstractList.__init__(self, sourceCollection)

    def insert(self, index: int, item: object) -> None:
        if index < 0: index = 0
        if index > len(self): index = len(self)

        theNode = self.getNode(index)
        newNode = TwoWayNode(item, theNode.previous, theNode)
        theNode.previous.next = newNode
        theNode.previous = newNode
        self.size += 1
        self.incModCount()

    
    def pop(self, index: int) -> None:
        if index < 0 or index >= len(self):
            raise IndexError("List index out of range")

        theNode = self.getNode(index)
        theNode.previous.next = theNode.next
        theNode.next.previous = theNode.previous
        theNode.previous = theNode.next = None
        self.size -= 1
        self.incModCount()

    
    def clear(self) -> None:
        """Clears the list of all values.
        """
        self.head = TwoWayNode()
        self.head.previous = self.head.next = self.head
        self.modCount = 0

    
    def listIterator(self) -> LinkedListIterator:
        """Creates a new linked list iterator.

        Returns:
            LinkedListIterator: The advanced iterator object for this list.
        """
        return LinkedListIterator(self)

    
    def __len__(self) -> int:
        """Returns the physical length of the list.

        Returns:
            int: The physical length of the list.
        """
        return self.size

    
    def __iter__(self):
        """The basic iterator for this list.

        Yields:
            Object: The next element in the list.
        """
        cursor: TwoWayNode = self.head.next
        while cursor != self.head:
            yield cursor.data
            cursor = cursor.next
    
    
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
        if i < 0 or i >= len(self):
            raise IndexError("List index out of range")
        return self.getNode(i).data

    
    def __setitem__(self, i:int, o: object) -> None:
        
        """Sets an item at a specific index of the list.

        Args:
            i (int): Index to set an item at.
            o (object): The object to set at the provided index.

        Raises:
            IndexError: When the index is out of range of the
            list.
        """
        if i < 0 or i >= len(self):
            raise IndexError("List index out of range")
        self.getNode(i).data = o

    def getNode(self, i: int) -> TwoWayNode:
        """Helper method for getting a node pointer.

        Args:
            i (int): Index of the node.

        Returns:
            TwoWayNode: The node at the specified index
        """
        ml = len(self)
        if i == ml:
            return self.head
        if i == ml - 1:
            return self.head.previous
        probe = self.head.next
        while i > 0:
            probe = probe.next
            i -= 1
        return probe