# ERROR
class Empty(Exception): pass
class Full(Exception): pass

# DEQUE
class Deque:

    # CONSTRUCTOR
    def __init__(self, capacity = 100):

        self.head = -1
        self.tail = 0
        self.D = [None] * capacity
        self.capacity = capacity

    # METHOD OVERRIDING
    def __str__(self):

        return str(self.D)
    
    # DEQUE-EMPTY
    def isEmpty(self):

        return True if self.head == -1 else False
    
    # DEQUE-FULL
    def isFull(self):

        return True if self.head == (self.tail + 1) % self.capacity else False

    # ADD-LEFT
    def addL(self, x):

        if self.isFull(): raise Full("Deque Overflow")
        else:
            if self.head == -1:
                self.head = 0
            elif self.head == 0:
                self.head = self.capacity - 1
            else:
                self.head -= 1
            self.D[self.head] = x

    # ADD-RIGHT
    def addR(self, x):

        if self.isFull(): raise Full("Deque Overflow")
        else:
            if self.head == -1:
                self.head = 0
            elif self.tail == self.capacity:
                self.tail = 0
            else:
                self.tail += 1
            self.D[self.tail] = x
            
    # POP-LEFT
    def popL(self):

        if self.isEmpty(): raise Empty("Deque Underflow")
        else:
            x = self.D[self.head]
            self.D[self.head] = None
            if self.head == self.tail:
                self.head = -1
            else:
                if self.head == self.capacity-1:
                    self.head = 0
                else:
                    self.head += 1
            return x
            

    # POP-RIGHT
    def popR(self):

        if self.isEmpty(): raise Empty("Deque Underflow")
        else:
            x = self.D[self.tail]
            self.D[self.tail] = None
            if self.head == self.tail:
                self.head = -1
            else: 
                if self.tail == 0:
                    self.tail = self.capacity - 1
                else:
                    self.tail -= 1
            return x
            
    # GET-HEAD
    def getHead(self):

        return self.D[self.head]
    
    # GET-TAIL
    def getTail(self):

        return self.D[self.tail]


# DRIVER

D = Deque(5)
D.addR(4)
D.addR(5)
D.addL(3)
D.addL(2)
D.addL(1)
print(D)
D.popL()
print(D)
D.popL()
print(D)
D.popR()
print(D)


