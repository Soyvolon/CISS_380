from abstract_bag import AbstractBag
from node import TwoWayNode

class DoublyLinkedBag(AbstractBag):
    def __init__(self, sourceCollection) -> None:
        self.head = None
        self.tail = None

        super().__init__(self, sourceCollection)

    def add(self, item: object) -> None:
        """Adds an object to the collection.

        Args:
            item (object): The song to add.
        """
        if not isinstance(self.__songs_head, TwoWayNode):
            self.__songs_head = TwoWayNode(item)
            self.__songs_tail = self.__songs_head
        else:
            self.__songs_tail.next = TwoWayNode(item, self.__songs_tail)
            self.__songs_tail = self.__songs_tail.next

        self.size += 1

    def remove(self, item: object):
        """Removes an object from the collection.

        Args:
            item (object): The item to remove.
        """
        res = self.__detach(item)
        self.size -= 1

    def __detach(self, item: object) -> TwoWayNode:
        """Detaches a Two Way Node from the collection.

        Args:
            item (object): The item the TwoWayNode contains to detach.

        Returns:
            TwoWayNode: The node that was detached.
        """
        if isinstance(self.__songs_head, TwoWayNode):
            # navigate to the node to detach.
            node = self.__songs_head
            lowerNode = self.__songs_tail
            half = len(self) / 2
            for x in range(half):
                if node.data == item:
                    break
                elif lowerNode.data == item:
                    node = lowerNode
                    break
                else:
                    node = node.next
                    lowerNode = lowerNode.previous
            # move links around for this node, and set 
            # internal values when needed.
            if isinstance(node.next, TwoWayNode) and isinstance(node.previous, TwoWayNode):
                node.next.previous = node.previous
                node.previous.next = node.next
            elif isinstance(node.next, TwoWayNode):
                node.next.previous = None
                self.__songs_head = node.next
            elif isinstance(node.previous, TwoWayNode):
                node.previous.next = None
                self.__songs_tail = node.previous
            else:
                self.__songs_head = None
                self.__songs_tail = None
            # clear detached node's links.
            node.next = None
            node.previous = None
            return node            
        else:
            raise IndexError("Index is out of range.")

    def __getitem__(self, index: int) -> object:
        if isinstance(self.__songs_head, TwoWayNode):
            node = None
            if index >= 0:
                node = self.__songs_head
                for i in range(0, index):
                    node = self.__songs_head.next
                    if not isinstance(node, TwoWayNode):
                        raise IndexError("Index is out of range")
            else:
                node = self.__songs_tail
                for i in range(0, index, -1):
                    node = self.__songs_tail.previous
                    if not isinstance(node, TwoWayNode):
                        raise IndexError("Index is out of range")
            return node.data
        else:
            raise IndexError("Index is out of range.")

    def __setitem__(self, index: int, item: object) -> None:
        if isinstance(self.__songs_head, TwoWayNode):
            node = None
            if index >= 0:
                node = self.__songs_head
                for i in range(0, index):
                    node = self.__songs_head.next
                    if not isinstance(node, TwoWayNode):
                        raise IndexError("Index is out of range")
            else:
                node = self.__songs_tail
                for i in range(0, index, -1):
                    node = self.__songs_tail.previous
                    if not isinstance(node, TwoWayNode):
                        raise IndexError("Index is out of range")
            node.data = item
        else:
            raise IndexError("Index is out of range.")

    def __iter__(self):
        node = self.__songs_head
        while isinstance(node, TwoWayNode):
            yield node.data
            node = node.next

    def __contains__(self, item: object) -> bool:
        for i in self:
            if i == item:
                return True
        return False