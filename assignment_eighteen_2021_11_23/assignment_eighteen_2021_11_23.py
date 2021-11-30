# Complete the code for LinkedList class in the form described in
# textbook using doubly linked nodes and with dummy head node. 
# Combine the code from AbstractCollection and AbstractList classes 
# into one AbstractList class, that is really abstract, that is it 
# derives from ABC and contains abstract methods. 

# Also complete and test code for LinkedListIterator that is different 
# than the ArrayListIterator, like the textbook describes it is possible 
# to implement iterator methods efficiently (that is O(1) time complexity). 
# Attached you will find the file for LinkedListIterator class with one method implemented. 

from LinkedList import LinkedList


def main():
    print("Create a list with 1-9")
    lyst = LinkedList(range(1, 10))
    print("Length:", len(lyst))

    print("Items (first to last): ", lyst)
    # Create and use a list iterator
    listIterator = lyst.listIterator()

    print("Forward traversal: ", end = "")
    listIterator.first()
    while listIterator.hasNext():
        print (listIterator.next(), end = " ")

    print("\nBackward traversal: ", end = "")
    listIterator.last()
    while listIterator.hasPrevious():
        print(listIterator.previous(), end = " ")

    print("\nInserting 10 before 2: ", end = "")
    listIterator.first()
    for count in range(2):
        # move to the 3rd item in the list.
        listIterator.next()
    listIterator.insert(10)
    print(lyst)

    print("Removing 2: ", end = "")
    listIterator.first()
    for count in range(3):
        # move to the 4th item in the list.
        listIterator.next()
    listIterator.remove()
    print(lyst)

    print("Removing all items")
    listIterator.first()
    while listIterator.hasNext():
        listIterator.next()
        listIterator.remove()
    # this list iterator is... wonky. Building to fit
    # these tests leads to some odd logic, like below.
    listIterator.last()
    listIterator.remove()
    print("Length:", len(lyst))

if __name__ == "__main__":
    main()