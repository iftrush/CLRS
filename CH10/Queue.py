# ERROR
class Empty(Exception): pass

# QUEUE
class Queue:

    # CONSTRUCTOR
    def __init__(self, capacity = 100):

        self.capacity = capacity
        self.head = self.size = 0
        self.Q = [None] * capacity
    
    # METHOD OVERRIDING
    def __len__(self):

        return self.size
    
    # METHOD OVERRIDING
    def __str__(self):

        return str(self.Q)

    # QUEUE-EMPTY
    def isEmpty(self):

        return self.size == 0
    
    # FRIST
    def first(self):

        if self.isEmpty():
            raise Empty("Queue Underflow")

        return self.Q[self.head]
    
    # DEQUEUE
    def dequeue(self):

        if self.isEmpty():
            raise Empty("Queue Underflow")
        x = self.Q[self.head]
        self.Q[self.head] = None
        self.head = (self.head + 1) % len(self.Q)
        self.size -= 1

        return x
    
    # ENQUEUE
    def enqueue(self, x):

        if self.size == len(self.Q):
            self.resize(2 * len(self.Q))
        avail = (self.head + self.size) % len(self.Q)
        self.Q[avail] = x
        self.size += 1
    
    # RESIZE
    def resize(self, capacity):

        old = self.Q
        self.Q = [None] * capacity
        walk = self.head
        for i in range(self.size):
            self.Q[i] = old[walk]
            walk = (walk + 1) % len(old)
        self.head = 0

# DRIVER
A = Queue()
B = Queue()
for i in range(200):
    A.enqueue(i)
print(A)
for i in range(len(A)):
    B.enqueue(A.dequeue())
print(B)