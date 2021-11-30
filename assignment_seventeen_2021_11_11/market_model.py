"""
File: marketmodel.py
"""
from random import randint
from cashier import Cashier
from customer import Customer
from time import sleep

class MarketModel(object):
    def __init__(self, lengthOfSimulation, averageTimePerCus,
    probabilityOfNewArrival, ammountOfRegisters, ticksPerSecond = .5):
        self.probabilityOfNewArrival = probabilityOfNewArrival
        self.lengthOfSimulation = lengthOfSimulation
        self.averageTimePerCus = averageTimePerCus
        self.ammountOfRegisters = ammountOfRegisters
        self.cashiers = []
        for i in range(ammountOfRegisters):
            self.cashiers.append(Cashier())
            
        if ticksPerSecond != 0:
            self.sleepTimer = 1 / ticksPerSecond
        else:
            self.sleepTimer = None
        
    def runSimulation(self):
        """Run the clock for n ticks."""
        print("--- SIMUATION START ---")
        
        for currentTime in range(self.lengthOfSimulation):
            # Attempt to generate a new customer
            customer = Customer.generateCustomer(
                self.probabilityOfNewArrival,
                currentTime,
                self.averageTimePerCus)
            # Send customer to cashier if successfully
            # generated
            if customer != None:
                # generate a random position for this customer
                pos = randint(0, self.ammountOfRegisters - 1)
                # find the shortest queue within a few lanes
                # of the customer
                shortest = None
                short = -1
                shortestIndex = 0
                for x in range(0, 3):
                    for z in [-1, 1]:
                        i = pos + (x * z) 
                        # if the lane does not exist, skip it
                        if i < 0 or i >= self.ammountOfRegisters:
                            continue
                        # otherwise compare all lane sizes
                        s = len(self.cashiers[i].queue)
                        if self.cashiers[i].currentCustomer != None:
                            s += 1
                        if short == -1 or s < short:
                            shortest = self.cashiers[i]
                            short = s
                            shortestIndex = i
                shortest.addCustomer(customer)
                print("A new customer arrived at {} and went to register {}".format(pos, shortestIndex))
            
            # Tell cashier to provide another unit of service
            for x in self.cashiers:
                x.serveCustomers(currentTime)
                
            self.display_simulation()
            
            # delay the execution of ticks for readable output.
            if self.sleepTimer:
                sleep(self.sleepTimer)
        
        print("--- SIMULATION END ---")
            
    def __str__(self):
        return str(self.cashier)
    
    def display_simulation(self):
        res = []
        for x in self.cashiers:
            res.append(str(x).split('\n'))
            
        output = ""
        for y in range(0, len(res[0])):
            line = ""
            for x in range(0, len(res)):
                line += "%-16s" % res[x][y]
            output += line + '\n'
        print(output)