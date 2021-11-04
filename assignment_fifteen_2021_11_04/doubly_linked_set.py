# write class definition of DoublyLinkedSet by subclassing from 
# AbstractCollection, AbstractBag and DoublyLinkedBag. that means
# that you also need to have these three classes written down and submitted. 

from doubly_linked_bag import DoublyLinkedBag

class DoublyLinkedSet(DoublyLinkedBag):
    def __init__(self, sourceCollection = None):
        super().__init__(sourceCollection)

    def add(self, item: object) -> None:
        if not item in self:
            super().add(item)
    