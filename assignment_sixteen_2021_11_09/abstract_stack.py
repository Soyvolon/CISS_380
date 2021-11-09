from abc import ABC, abstractmethod
from typing import Iterator

class AbstractStack(ABC):
    @abstractmethod
    def __init__(self, sourceCollection = None):
        self.size = 0
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
    def isEmpty(self) -> bool:
        """Get if the stack is empty.

        Returns:
            bool: True if the stack is empty, false if not.
        """
        pass

    