# 1. Projects 8 - 11 on page 125 in the textbook. 

# 2. Write two separate functions that will perform a bubble sort on
#  linked structures. One function should take as a parameter a singly
#  linked node and the other function should take as a parameter doubly
#  linked node. The functions should not return anything but modify an
#  existing structure. 

from node import *

def length(head: Node) -> None:
    c = 1
    cur = head

    while isinstance(cur.next, Node):
        c += 1
        cur = cur.next

    return c

def insert(item, pos: int, head: Node) -> Node:
    if pos < 0:
        raise IndexError("Index must be above 0.")

    new = Node(item)
    i = 0
    prev = None
    cur = head
    while isinstance(cur, Node):
        if i == pos:
            if prev != None:
                # insert item in the middle
                tmp = prev.next
                prev.next = new
                new.next = tmp
                return head
            else:
                new.next = cur
                # we inserted at the beginning, 
                # new is the new head
                return new
                
        elif cur.next == None:
            # insert item at end
            cur.next = new
            return head      
        i += 1
        prev = cur
        cur = cur.next

    return head

def pop(pos: int, head: Node):
    if pos < 0:
        raise IndexError("index must be above 0.")

    i = 0
    prev = None
    cur = head
    while isinstance(cur, Node):
        if i == pos:
            if prev != None:
                prev.next = cur.next
                cur.next = None
                return (head, cur.data)
            else:
                tmp = cur.next
                cur.next = None
                return (tmp, cur.data)

        i += 1
        prev = cur
        cur = cur.next
    
    raise IndexError("Index out or range of Node.")

def make_two_way(head: Node) -> TwoWayNode:
    startHead = TwoWayNode(head.data, None, None)
    prev = startHead
    cur = head.next

    while isinstance(cur, Node):
        tmp = TwoWayNode(cur.data, prev, None)
        prev.next = tmp
        prev = tmp
        cur = cur.next

    return startHead
        
def print_node_tree(head: Node):
    cur = head
    while isinstance(cur, Node):
        print(cur.data)
        cur = cur.next

def print_double_tree_display(head: TwoWayNode):
    cur = head
    while isinstance(cur, TwoWayNode):
        p = cur.previous
        if p != None:
            p = p.data
        n = cur.next
        if n != None:
            n = n.data
        print("{a} < {b} > {c}".format(a = p, b = cur.data, c = n))
        cur = cur.next

def bubble_single_y(head: Node):
    sorted = True
    first = False
    while sorted and first:
        tmp = head
        next = tmp.next
        c = 0
        while isinstance(next, Node):
            if tmp.data > next.data:
                next = next.next
                c += 1
        
                


        first = True


def bubble_single(head: Node):
    cur = head
    c = 0
    while isinstance(cur, Node):
        tmp = cur
        while isinstance(tmp.next, Node):
            if tmp.data > tmp.next.data:
                head, dat = pop(c, head)
                head = insert(dat, c + 1, head)
                # reset tmp
                tmp = head
                for i in range(0, c):
                    # move back to tmp loc
                    tmp = tmp.next
                cur = head
                c = 0
            break
        cur = cur.next
        c += 1


def bubble_single_x(head: Node):
    cur = head
    pos = 0
    while type(cur) == Node:
        jump = cur.next
        if not isinstance(jump, Node):
            break
        jumpC = -1
        while cur.data > jump.data:
            tmp = jump.next
            if type(tmp) == Node:
                jump = tmp
                jumpC = 0
            else:
                jumpC = 1
                break
        if jumpC >= 0:
            dat = cur.data
            cur, dmp = pop(0, cur)
            jump = insert(dat, jumpC, jump)
        cur = cur.next
        pos += 1

def double_bubble(head: TwoWayNode):
    cur = head
    while isinstance(cur, TwoWayNode):
        jump = cur.next
        if not isinstance(jump, Node):
            break

        jumpC = -1
        while cur.data < jump.data:
            tmp = jump.previous
            if type(tmp) == Node:
                jump = tmp
                jumpC = 0
            else:
                jumpC = 1
                break
        if jumpC >= 0:
            dat = cur.data
            cur, dmp = pop(0, cur)
            jump = insert(dat, jumpC, jump)
        cur = cur.next

def main():
    end = Node(1)
    two = Node(3, end)
    head = Node(2, two)

    print_node_tree(head)
    print()
    bubble_single(head)
    print_node_tree(head)

    # two = make_two_way(head)

    # print_double_tree_display(two)
    # double_bubble(two)
    # print()
    # print_double_tree_display(two)

    # print(length(head))
    # print("------")
    # print_node_tree(head)
    # print("------")

    # head = insert("start", 0, head)
    # head = insert("end", 1000, head)
    # head = insert("middle", 3, head)

    # print_node_tree(head)
    # print("------")

    # head, item = pop(2, head)
    # print(item)
    # print("------")
    # print_node_tree(head)
    # print("------")
    # head, item = pop(0, head)
    # print(item)
    # print("------")
    # print_node_tree(head)
    # print("------")

    # head = make_two_way(head)
    # print_double_tree_display(head)

if __name__ == "__main__":
    main()