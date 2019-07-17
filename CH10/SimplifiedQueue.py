# ERROR
class Empty(Exception): pass
class Full(Exception): pass

# QUEUE
class Queue:

    # CONSTRUCTOR
    def __init__(self, capacity = 100, head = -1, tail = 0):

        self.head = head
        self.tail = tail
        self.capacity = capacity
        self.Q = [None] * capacity
        self.size = 0

    # METHOD OVERRIDING
    def __len__(self):

        return len(self.Q)

    # METHOD OVERRIDING
    def __str__(self):

        return str(self.Q)

    # QUEUE-EMPTY
    def isEmpty(self):

        return True if self.head == -1 else False
    
    # QUEUE-FULL
    def isFull(self):

        return True if self.head == (self.tail + 1) % self.capacity else False
    
    # ENQUEUE
    def enqueue(self, x):

        if self.isFull(): raise Full("Queue Overflow")
        else:
            if self.head == -1:
                self.head = 0
            elif self.tail == self.capacity:
                self.tail = 0
            else:
                self.tail += 1
            self.Q[self.tail] = x

    # DEQUEUE
    def dequeue(self):

        if self.isEmpty(): raise Empty("Queue Underflow")
        else:
            x = self.Q[self.head]
            if self.head == self.tail:
                self.head = -1
            else:
                if self.head == self.capacity-1:
                    self.head = 0
                else:
                    self.head += 1
            return x

# DRIVER
A = Queue()
B = Queue()
for i in range(100):
    A.enqueue(i)
print(A)
for i in range(len(A)):
    B.enqueue(A.dequeue())
print(B)
