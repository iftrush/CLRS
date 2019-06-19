import HeapSort
from HeapSort import HeapSize, MaxHeapify, PARENT

# HEAP-MAXIMUM implements MAXIMUM Θ(1)
def HeapMaximum(A):
    return A[0]

# HEAP-EXTRACT-MAX implements EXTRACT-MAX O(lgn)
def HeapExtractMax(A):

    global HeapSize
    if HeapSize == -1:
        HeapSize = len(A)
    if HeapSize < 1:
        return "Heap Underflow"
    max = A[0]
    A[0] = A[HeapSize-1]
    A.pop()
    HeapSize -= 1
    MaxHeapify(A,0)  #O(lgn)
    return max

# HEAP-INCREASE-KEY implements INCREASE-KEY O(lgn)
def HeapIncreaseKey(A,i,key):

    if key < A[i]:
        return "new key is smaller than current key"
    A[i] = key

    while i >= 0 and A[PARENT(i)] < A[i]:
        A[i], A[PARENT(i)] = A[PARENT(i)], A[i]
        i = PARENT(i) #O(lgn)

# HEAP-INSERT implenments INSERT O(lgn)
def MaxHeapInsert(A,key):
    
    global HeapSize
    if HeapSize == -1:
        HeapSize = len(A)
    HeapSize += 1
    A.append(0)
    A[HeapSize-1] = -1000000
    HeapIncreaseKey(A,HeapSize-1,key)  #O(lgn)

