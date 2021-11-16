from abc import ABC, abstractmethod

class AbstractQueue(ABC):
    def __init__(self):
        self.size = 0
    
    @abstractmethod  
    def enqeue(self, item: object) -> None:
        """Adds and item to the queue.

        Args:
            item (object): The item to add.
        """
        pass
    
    @abstractmethod
    def dequeue(self) -> object:
        """Removes the item at the front of the queue.

        Returns:
            object: The item at the front of the queue.
        """
        pass
    
    @abstractmethod
    def clear(self) -> None:
        """Clears the values in the queue.
        """
        pass
    
    @abstractmethod
    def peek(self) -> object:
        """Returns the item at the front of the queue without removing it.

        Returns:
            object: The object at the front of the queue.
        """
    
    def __len__(self):
        return self.size
    
    def __eq__(self, o: object):
        if isinstance(o, AbstractQueue):
            if o.size == self.size:
                other = iter(o)
                for x in self:
                    if x != next(other):
                        return False
                return True
            else:
                return False
        return False

    def isEmpty(self) -> bool:
        return self.size == 0
    
    def __str__(self):
        return "{" + map(str, self) + "}"