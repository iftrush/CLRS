# DOUBLY LINKED LIST
class LinkedList:

    # NODE
    class Node:

        # STREAMLINE MEMORY
        __slots__ = 'key', 'prev', 'next'

        # CONSTRUCTOR for NODE
        def __init__(self, key, prev, next):

            self.key = key
            self.prev = prev
            self.next = next
    
    # CONSTRUCTOR for LINKEDLIST
    def __init__(self):

        self.head = self.Node(None, None, None)
        self.tail = self.Node(None, None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    
    # METHOD OVERRIDING
    def __len__(self):

        return self.size
    
    # EMPTY
    def isEmpty(self):

        return self.size == 0

    # INSERT-BETWEEN
    def InsertBetween(self, e, predecessor, successor):

        newest = self.Node(e, predecessor, successor)
        predecessor.next = newest
        successor.prev = newest
        self.size += 1

        return newest
    
    # DELETE-NODE
    def DeleteNode(self, node):

        predecessor = node.prev
        successor = node.next
        predecessor.next = successor
        successor.prev = predecessor
        self.size -= 1
        key = node.key
        node.prev = node.next = node.key = None

        return key

# EXCEPTION HANDLING
class Empty(Exception): pass

# Implementing Deque Using A Doubly Linked List
class LinkedDeque(LinkedList): # INHERITANCE
    
    # FIRST
    def first(self):

        if self.isEmpty():
            raise Empty("Deque is Empty")

        return self.head.next.key

    # LAST
    def last(self):

        if self.isEmpty():
            raise Empty("Deque is Empty")

        return self.tail.prev.key
    
    # INSERT-FIRST
    def InsertFirst(self, e):

        self.InsertBetween(e, self.head, self.head.next)

    # INSERT-LAST

    def InsertLast(self, e):

        self.InsertBetween(e, self.tail.prev, self.tail)

    # DELETE-FIRST
    def DeleteFirst(self):

        if self.isEmpty():
            raise Empty("Deque is Empty")

        return self.DeleteNode(self.head.next)

    # DELETE-LAST
    def DeleteLast(self):

        if self.isEmpty():
            raise Empty("Deque is Empty")

        return self.DeleteNode(self.tail.prev)

# POSITIONAL LIST
class PositionalList(LinkedList): #INHERITANCE

    # POSITION
    class Position:

        # CONSTRUCTOR for POSITION
        def __init__(self, container, node):

            self.container = container
            self.node = node
        
        # ELEMENT
        def element(self):

            return self.node.key
        
        # OPERATOR OVERRIDING
        def __eq__(self, other):

            return type(other) is type(self) and other.node is self.node
        
        # OPERATOR OVERRIDING
        def __ne__(self, other):

            return not(self == other)

    # VALIDATE
    def validate(self, p):

        if not isinstance(p, self.Position):
            raise TypeError("p must be proper Position type")
        if p.container is not self:
            raise ValueError("p does not belong to this container")
        if p.node.next is None:
            raise ValueError("p is no longer valid")

        return p.node

    # MAKE-POSITION
    def MakePosition(self, node):

        if node is self.head or node is self.tail:

            return None
        else:

            return self.Position(self, node)

    # FIRST
    def first(self):

        return self.MakePosition(self.head.next)
    
    # LAST
    def last(self):

        return self.MakePosition(self.tail.prev)
    
    # BEFORE
    def before(self, p):

        node = self.validate(p)

        return self.MakePosition(node.prev)
    
    # AFTER
    def after(self, p):

        node = self.validate(p)

        return self.MakePosition(node.next)

    # ITERATION OVERRIDING
    def __iter__(self):

        cursor = self.first
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    # METHOD OVERRIDING
    def InsertBetween(self, e, predecessor, successor):

        node =  super().InsertBetween(e, predecessor, successor)

        return self.MakePosition(node)
    
    # ADD-FIRST
    def addFirst(self, e):

        return self.InsertBetween(e, self.head, self.head.next)

    # ADD-LAST
    def addLast(self, e):

        return self.InsertBetween(e, self.tail.prev, self.tail)
    
    # ADD-BEFORE
    def addBefore(self, p, e):

        original = self.validate(p)

        return self.InsertBetween(e, original.prev, original)

    # ADD-AFTER
    def addAfter(self, p, e):

        original = self.validate(p)

        return self.InsertBetween(e, original, original.next)
    
    # DELETE
    def delete(self, p):

        original = self.validate(p)

        return self.DeleteNode(original)
    
    # REPLACE
    def replace(self, p, e):

        original = self.validate(p)
        old = original.key
        original.key = e

        return old

# INSERTION-SORT on a POSITIONAL LIST
def InsertionSort(L):

    if len(L) > 1:
        marker = L.first()
        
        while marker != L.last():
            pivot = L.after(marker)
            value = pivot.element()
            if value > marker.element():
                marker = pivot
            else:
                walk = marker
                while walk != L.first() and L.before(walk).element() > value:
                    walk = L.before(walk)
                L.delete(pivot)
                L.addBefore(walk, value)