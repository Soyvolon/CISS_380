from node import TwoWayNode

class LinkedListIterator(object):
        """Represents the list iterator for linked list."""

        def __init__(self, backingStore):
            self.backingStore = backingStore
            self.modCount = backingStore.getModCount()
            self.first()

        def first(self):
            """Returns the cursor to the beginning of the backing store."""
            self.cursor = self.backingStore.head.next
            self.lastItemPos = None
            
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