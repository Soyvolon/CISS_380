from node import *

class sls(object):
    def __init__(self):
        self.head = None
    def add(self, item):
        addNode = Node(item)
        if self.head == None:
            self.head = addNode
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = addNode
    
    def shift_left(self):
        start = self.head
        dat = None
        while isinstance(start, Node) and isinstance(start.next, Node):
            start.data = dat
            dat = start.next.data
            start.next.data = start.data
            start = start.next

        if isinstance(start, Node):
            self.head.data = dat
        
a = sls()
a.add(1)
a.add(2)
a.add(3)
a.add(4)

a.shift_left()

n = a.head
while n:
    print(n.data)
    n = n.next
