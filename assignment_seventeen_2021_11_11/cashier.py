"""
File: cashier.py
"""
from node_queue import NodeQueue

class Cashier(object):
    def __init__(self):
        self.totalCustomerWaitTime = 0
        self.customersServed = 0
        self.currentCustomer = None
        self.queue = NodeQueue()
        
    def addCustomer(self, c):
        self.queue.enqeue(c)
        
    def serveCustomers(self, currentTime):
        if self.currentCustomer is None:
            self.__setCurrentCustomer(currentTime)
        
        if self.currentCustomer is None:
            return
        
        # Give a unit of service
        self.currentCustomer.serve()
        # If current customer is finished, send it away
        if self.currentCustomer.getAmountOfServiceNeeded() <= 0:
            self.currentCustomer = None
            self.__setCurrentCustomer(currentTime)
          
    def __setCurrentCustomer(self, currentTime):
        # No customers yet
        if self.queue.isEmpty():
            return
        else:
            # Pop first waiting customer
            # and tally results
            self.currentCustomer = self.queue.dequeue()
            self.totalCustomerWaitTime += \
                currentTime - \
                self.currentCustomer.getArrivalTime()
            self.customersServed += 1
        
    def __str__(self):
        result = \
'''
| Cashier [{}] |
|      {}      |
|      {}      |
|      {}      |
|      {}      |
|      {}      |
|      {}     |
|-------------|
Avg T: {}
Srvd: {}
'''
        val = [' ']*5
        over = 0
        for i in range(0, self.queue.size):
            if i >= 5:
                over += 1
            else:
                val[i] = 'x'
                
        aveWaitTime = -1
        if self.customersServed != 0:
            aveWaitTime = self.totalCustomerWaitTime / \
                self.customersServed
        first = ' '
        if self.currentCustomer != None:
            first = 'x'
        result = result.format(first, val[0], val[1], val[2], val[3], val[4], '+' + str(over), \
            "%5.2f" % aveWaitTime, self.customersServed)
        
        return result