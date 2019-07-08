# ERROR
class Empty(Exception):

    pass

class Full(Exception):

    pass

# STACK
class Stack:

    # CONSTRUCTOR
    def __init__(self, size = 100):
        self.size = size
        self.S = [0] * size
        self.top = -1

    # METHOD OVERRIDING
    def __len__(self):

        return self.top + 1

    # STACK-EMPTY
    def isEmpty(self):

        return True if self.top == -1 else False

    # PUSH
    def push(self,x):

        if self.top == self.size:
            raise Full("Stack Overflow")
        else:
            self.top += 1
            self.S[self.top] = x
    
    # PEAK
    def peak(self):

        if self.isEmpty():
            raise Empty("Stack Underflow")

        return self.S[self.top]

    # POP
    def pop(self):

        if self.isEmpty():
            raise Empty("Stack Underflow")
        else:
            self.top -= 1
            return self.S[self.top + 1]

# DRIVER
A = Stack()
B = Stack()
for i in range(100):
    A.push(i)
for i in range(100):
    B.push(A.pop())
print(B.peak())
print(len(B))
