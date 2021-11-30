
from node import TwoWayNode

class LinkedListIterator(object):
        """Represents the list iterator for linked list."""

        def __init__(self, backingStore):
            import LinkedList
            self.backingStore : LinkedList.LinkedList = backingStore
            self.modCount = backingStore.getModCount()
            self.cursor : TwoWayNode = None
            self.lastItemPos : TwoWayNode = None
            self.first()

        def hasNext(self) -> bool:
            return self.cursor.next != self.backingStore.head

        def next(self):
            self.lastItemPos = self.cursor
            self.cursor = self.cursor.next
            return self.cursor.data

        def hasPrevious(self) -> bool:
            return self.cursor.previous != self.backingStore.head

        def previous(self):
            self.cursor = self.lastItemPos
            self.lastItemPos = self.cursor.previous
            return self.cursor.data

        def first(self):
            """Returns the cursor to the beginning of the backing store."""
            self.cursor = self.backingStore.head.next
            self.lastItemPos = None
            return self.cursor.data

        def last(self):
            self.cursor = self.backingStore.head.previous
            self.lastItemPos = self.cursor.previous
            return self.cursor.data
            
        def insert(self, item):
            """Preconditions:
            The list has not been modified except by this iterator's mutators.
            Adds item to the end if the current position is undefined, or
            inserts it at that position."""
            if self.modCount != self.backingStore.getModCount():
                raise AttributeError("List has been modified illegally.")
            if self.lastItemPos is None:
                self.backingStore.add(item)
            else:
                newNode = TwoWayNode(item, self.lastItemPos.previous, self.lastItemPos)
                self.lastItemPos.previous.next = newNode
                self.lastItemPos.previous = newNode
                self.backingStore.incModCount()
                self.backingStore.size += 1
                self.lastItemPos = None
            self.modCount += 1

        def remove(self):
            if self.modCount != self.backingStore.getModCount():
                raise AttributeError("List has been modified illegally.")
            if self.lastItemPos is None:
                raise IndexError("There is no item to remove. Iterator is not initialized.")
            else:
                tmp = self.lastItemPos
                self.lastItemPos.previous.next = self.lastItemPos = self.cursor
                self.lastItemPos.previous = self.lastItemPos
                tmp.next = tmp.previous = None

                self.backingStore.size -= 1
                self.backingStore.incModCount()
                self.lastItemPos = None
            self.modCount += 1
                

        def replace(self, item: object):
            if self.modCount != self.backingStore.getModCount():
                raise AttributeError("List has been modified illegally.")
            if self.lastItemPos is None:
                raise IndexError("There is no item to replace. Iterator is not initialized.")
            else:
                self.lastItemPos.data = item
                # we don't do any increments here, as this operation
                # is essentially the same as __setitem__
                # (the textbook does not increment values
                # for changes in __setitem__)