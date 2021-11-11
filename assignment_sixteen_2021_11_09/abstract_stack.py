from abc import ABC, abstractmethod
from typing import Collection, Iterator

class AbstractStack(ABC):
    def __init__(self, sourceCollection = None):
        self.size = 0
        if sourceCollection:
            for x in sourceCollection:
                self.push(x)
    
    @abstractmethod
    def __iter__(self) -> Iterator:
        """Iterate through the stack.

        Yields:
            Iterator: The iterator for this stack.
        """
        pass

    @abstractmethod
    def peek(self) -> object:
        """Get the item at the top of the stack.

        Raises:
            KeyError: if the stack is empty.

        Returns:
            object: The item at the top of the stack.
        """
        pass

    @abstractmethod
    def clear(self) -> None:
        """Clears the stack.
        """
        pass

    @abstractmethod
    def push(self, item: object) -> None:
        """Pushes a new item to the stack.

        Args:
            item (object): The item to push to the stack.
        """
        pass

    @abstractmethod
    def pop(self) -> object:
        """Removes and returns the item at the top of the stack.

        Raises:
            KeyError: if the stack is empty.

        Returns:
            object: The item at the top of the stack.
        """
        pass

    @abstractmethod
    def __len__(self):
        pass
    
    def __add__(self, o: object):
        if isinstance(o, AbstractStack):
            res = type(self)()
            for x in self:
                res.push(x)
            for x in o:
                res.push(o)
                
            return res
        raise TypeError("Can only add two abstract stacks.")
    
    def __eq__(self, o: object):
        if isinstance(o, AbstractStack):
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
    