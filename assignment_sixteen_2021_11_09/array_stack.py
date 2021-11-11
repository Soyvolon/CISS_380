from typing import Iterator
from abstract_stack import AbstractStack
from arrays import Array

class ArrayStack(AbstractStack):
    DEFAULT_CAPACITY = 10
    
    def __init__(self, sourceCollection = None):
        self.items = Array(self.DEFAULT_CAPACITY)
        
        AbstractStack.__init__(sourceCollection)
    
    def __iter__(self) -> Iterator:
        """Iterate through the stack.

        Yields:
            Iterator: The iterator for this stack.
        """
        for x in self.items:
            if not isinstance(x, None):
                yield x

    def peek(self) -> object:
        """Get the item at the top of the stack.

        Raises:
            KeyError: if the stack is empty.

        Returns:
            object: The item at the top of the stack.
        """
        if self.size == 0:
            raise KeyError("Stack is emtpy")
        
        return self.items[self.size - 1]

    def clear(self) -> None:
        """Clears the stack.
        """
        self.items = Array(self.DEFAULT_CAPACITY)
        self.size = 0
  
    def push(self, item: object) -> None:
        """Pushes a new item to the stack.

        Args:
            item (object): The item to push to the stack.
        """
        if (len(self) == self.size):
            # we are full - time to expand the array.
            newSize = self.size * 2
            new = Array(newSize)
            for x in range(0, len(self.items)):
                new[x] = self.items[x]
            self.items = new            
        
        self.items[self.size] = item
        self.size += 1

    def pop(self) -> object:
        """Removes and returns the item at the top of the stack.

        Raises:
            KeyError: if the stack is empty.

        Returns:
            object: The item at the top of the stack.
        """
        if self.size == 0:
            raise KeyError("Stack is empty")
        
        self.items[self.size - 1] = None
        self.size -= 1
        
        halfSize = len(self) / 2
        if halfSize > self.DEFAULT_CAPACITY \
            and halfSize > self.size:
            # we are small enough to shrink again
            # but make sure we dont shirt under
            # the default capacity.
            newSize = halfSize
            new = Array(newSize)
            for x in range(0, self.size):
                new[x] = self.items[x]
            self.items = new 
    
    def __len__(self):
        return len(self.items)