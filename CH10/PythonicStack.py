# ERROR
class Empty(Exception):

    pass

# PYTHONIC STACK
class Stack:

    # CONSTRUCTOR
    def __init__(self):

        self.S = []

    # METHOD OVERRIDING
    def __len__(self):

        return len(self.S)

    # STACK-EMPTY
    def isEmpty(self):

        return len(self.S) == 0

    # PUSH
    def push(self,x):

        self.S.append(x)

    # PEAK
    def peak(self):

        if self.isEmpty():
            raise Empty("Stack Underflow")

        return self.S[-1]

    # POP
    def pop(self):

        if self.isEmpty():
            raise Empty("Stack Underflow")

        return self.S.pop()

# DRIVER
A = Stack()
B = Stack()
for i in range(100):
    A.push(i)
for i in range(100):
    B.push(A.pop())
print(B.peak())
print(len(B))