# 2. Write a simple class to represent a song. there should be just three attributes: 
# title, performer and duration. The class should contain the basic get*, set*, str* and 
# init* methods. Write the main program that will allow user to maintain the collection 
# of songs as a linked structure of doubly linked nodes. The program should have 
# functions for adding a new song, removing a song, modifying the information about 
# existing song, finding and displaying songs with the given author or title.

from music import Music
from node import TwoWayNode

class SongCollection(object):
    def __init__(self):
        self.__songs_head = None
        self.__songs_tail = None
    
    def append(self, song: Music) -> None:
        """Adds a song to the collection.

        Args:
            song (Music): The song to add.
        """
        if not isinstance(self.__songs_head, TwoWayNode):
            self.__songs_head = TwoWayNode(song)
            self.__songs_tail = self.__songs_head
        else:
            self.__songs_tail.next = TwoWayNode(song, self.__songs_tail)
            self.__songs_tail = self.__songs_tail.next

    def remove(self, index: int) -> Music:
        """Removes a song from the collection by index.

        Args:
            index (int): The index of the song to remove.

        Returns:
            Music: The song that was removed.
        """
        res = self.__detach(index)
        return res.data

    def find_by_performer(self, performer: str):
        node = self.__songs_head
        while isinstance(node, TwoWayNode):
            if node.data.get_performer() == performer:
                return node.data
            
            node = self.__songs_head.next

        return None

    def find_by_title(self, title: str):
        node = self.__songs_head
        while isinstance(node, TwoWayNode):
            if node.data.get_title() == title:
                return node.data
            
            node = self.__songs_head.next

        return None

    def __detach(self, index: int) -> TwoWayNode:
        """Detaches a Two Way Node from the collection.

        Args:
            index (int): The index of the Two Way Node to detach

        Returns:
            TwoWayNode: The node that was detached.
        """
        if isinstance(self.__songs_head, TwoWayNode):
            # navigate to the node to detach.
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

    def __getitem__(self, index: int) -> Music:
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

    def __setitem__(self, index: int, item: Music) -> None:
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