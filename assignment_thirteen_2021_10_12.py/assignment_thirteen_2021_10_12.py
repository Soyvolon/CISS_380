# 1. Write function merge that will take as parameters two singly linked nodes. 
# Both nodes should contain a list of ordered integers. the function should create 
# and return a new singly linked node that contains items from both input nodes in order. 

# 2. Write a simple class to represent a song. there should be just three attributes: 
# title, performer and duration. The class should contain the basic get, set, str and 
# init methods. Write the main program that will allow user to maintain the collection 
# of songs as a linked structure of doubly linked nodes. The program should have 
# functions for adding a new song, removing a song, modifying the information about 
# existing song, finding and displaying songs with the given author or title.  

from node import *

def merge_int_singles(lowerHead: Node, upperHead: Node) -> Node:
    # assume the two lists are sorted.
    if lowerHead is None and upperHead is None:
        return None
    if lowerHead is None:
        return upperHead
    if upperHead is None:
        return lowerHead

    low = lowerHead
    high = upperHead
    outputStart = None
    output = None

    # setup the first data value
    if high.data > low.data:
        output = Node(low.data)
        low = low.next
    else:
        output = Node(high.data)
        high = high.next
    # save our head value
    outputStart = output
    # make sure both values are an instance of the Node
    while isinstance(low, Node) or isinstance(high, Node):
        # if one of the two are invalid,
        # append the valid one to the end of the list.
        if not isinstance(low, Node):
            output.next = high
            return outputStart
        if not isinstance(high, Node):
            output.next = low
            return outputStart

        # compare and save data
        if high.data > low.data:
            output.next = Node(low.data)
            low = low.next
        else:
            output.next = Node(high.data)
            high = high.next

        output = output.next

    return outputStart

def print_node_tree(head: Node):
    cur = head
    while isinstance(cur, Node):
        print(cur.data)
        cur = cur.next

def main():
    Abase = Node(4, None)
    Aone = Node(3, Abase)
    Atwo = Node(2, Aone)
    Athree = Node(2, Atwo)
    Ahead = Node(1, Athree)

    
    Btwo = Node(3, None)
    Bthree = Node(1, Btwo)
    Bhead = Node(1, Bthree)

    print("\n-- START: Test Node Joining --\n")
    print("----- A -----")
    print_node_tree(Ahead)
    print("----- B -----")
    print_node_tree(Bhead)
    print("----- R -----")
    result = merge_int_singles(Ahead, Bhead)
    print_node_tree(result)
    print("\n-- END: Test Node Joining --\n")

    

if __name__ == "__main__":
    main()