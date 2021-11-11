from typing import Iterator
from abstract_stack import AbstractStack
from node import Node

class NodeStack(AbstractStack):
    def __init__(self, sourceCollection = None):
        self.items = None

        super().__init__(self, sourceCollection)

    def __iter__(self) -> Iterator:
        def visitNodes(node: Node):
            if isinstance(node, Node):
                yield from visitNodes(node.next)
                yield node.data

        yield from visitNodes(self.items)
        
    def peek(self) -> object:
        """Get the item at the top of the stack.

        Raises:
            KeyError: if the stack is empty.

        Returns:
            object: The item at the top of the stack.
        """
        if isinstance(self.items, Node):
            return self.items.data
        raise KeyError("Stack is empty.")

    def clear(self) -> None:
        """Clears the stack.
        """
        self.items = None
        self.size = 0

    def push(self, item: object) -> None:
        """Pushes a new item to the stack.

        Args:
            item (object): The item to push to the stack.
        """
        self.items = Node(item, self.items)
        self.size += 1

    def pop(self) -> object:
        """Removes and returns the item at the top of the stack.

        Raises:
            KeyError: if the stack is empty.

        Returns:
            object: The item at the top of the stack.
        """
        if isinstance(self.items, Node):
            dat = self.items.data
            self.items = self.items.next
            self.size -= 1
            return dat
        raise KeyError("Stack is empty")

    def __len__(self):
        c = 0
        for x in self:
            c += 1
            
        return c