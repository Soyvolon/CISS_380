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