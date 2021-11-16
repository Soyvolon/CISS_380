from abstract_queue import AbstractQueue
from node import TwoWayNode

class NodeQueue(AbstractQueue):
    def __init__(self):
        self.head = None
        self.tail = None
        super().__init__()
        
    def enqeue(self, item: object) -> None:
        """Adds and item to the queue.

        Args:
            item (object): The item to add.
        """
        if self.isEmpty():
            self.head = TwoWayNode(item)
            self.tail = self.head
        else:
            tmp = self.tail
            self.tail = TwoWayNode(item, self.tail)
            tmp.next = self.tail
        self.size += 1
    
    def dequeue(self) -> object:
        """Removes the item at the front of the queue.

        Raises:
            KeyError: When there is no elements in the queue.

        Returns:
            object: The item at the front of the queue.
        """
        if self.isEmpty():
            raise KeyError("No elemnts in the queue.")
        else:
            tmp : TwoWayNode = self.head
            self.head = self.head.next
            if isinstance(self.head, TwoWayNode):
                self.head.previous = None
            self.size -= 1
            if self.isEmpty():
                self.tail = None
            
            return tmp.data
    
    def clear(self) -> None:
        """Clears the values in the queue.
        """
        self.head = None
        self.tail = None
        self.size = 0
    
    def peek(self) -> object:
        """Returns the item at the front of the queue without removing it.

        Raises:
            KeyError: When there is no elements in the queue.

        Returns:
            object: The object at the front of the queue.
        """
        if self.isEmpty():
            raise KeyError("No elemnts in the queue.")
        else:            
            return self.head.data
                
        