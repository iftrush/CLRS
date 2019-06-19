# 0-Based
#       PARENT
#      /      \
#    LEFT   RIGHT
HeapSize = -1


def PARENT(i):
    return (i - 1) // 2
def LEFT(i):
    return 2 * i + 1
def RIGHT(i):
    return 2 * i + 2

# MAX-HEAPIFY using While-loop
def MaxHeapifyWhile(A,i):

    while(True):
        l = LEFT(i)
        r = RIGHT(i)
        if l < HeapSize and A[l] > A[i]:
            largest = l
        else:
            largest = i
        if r < HeapSize and A[r] > A[largest]: 
            largest = r
        if largest != i:
            A[largest], A[i] = A[i], A[largest] #swap
            i = largest
        else:
            break

# MAX-HEAPIFY O(lgn)
def MaxHeapify(A,i):

    global HeapSize
    if HeapSize == -1:
        HeapSize = len(A)
    l = LEFT(i)
    r = RIGHT(i)
    if l < HeapSize and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < HeapSize and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[largest], A[i] = A[i], A[largest]
        MaxHeapify(A,largest)

# MIN-HEAPIFY O(lgn)
def MinHeapify(A,i):

    global HeapSize
    if HeapSize == -1:
        HeapSize = len(A)
    l = LEFT(i)
    r = RIGHT(i)
    if l < HeapSize and A[l] < A[i]:
        smallest = l
    else:
        smallest = i
    if r < HeapSize and A[r] < A[smallest]:
        smallest = r
    if smallest != i:
        A[smallest], A[i] = A[i], A[smallest]
        MinHeapify(A,smallest)

# BUILD-MAX-HEAP O(n * lgn) = O(nlgn) -> O(n) since n-element heap has height floor(lgn)
#                                                                  has at most ceil(n/2^(h+1)) nodes
def BuildMaxHeap(A):
    n = len(A)
    for i in range(n//2-1,-1,-1): # O(n) calls to MaxHeapify
        MaxHeapify(A,i) #O(lgn)

def BuildMinHeap(A):
    n = len(A)
    for i in range(n//2-1,-1,-1): # O(n) calls to MaxHeapify
        MinHeapify(A,i) #O(lgn)


# HEAPSORT in Increasing Order
def HeapSortIC(A):

    global HeapSize
    HeapSize = len(A)
    BuildMaxHeap(A)

    for i in range(len(A)-1,0,-1):
        A[0], A[i] = A[i], A[0]
        HeapSize -= 1
        MaxHeapify(A,0)

# HEAPSORT in Decreasing Order
def HeapSortDC(A):

    global HeapSize
    HeapSize = len(A)
    BuildMinHeap(A)

    for i in range(len(A)-1,0,-1):
        A[0], A[i] = A[i], A[0]
        HeapSize -= 1
        MinHeapify(A,0)
