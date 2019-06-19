import random

# QUICKSORT Θ(nlgn)                     # Worst Case: T(n) =  T(n-1) + Θ(n) = Θ(n^2)
def QuickSort(A, p, r):                 #  Best Case: T(n) = 2T(n/2) + Θ(n) = Θ(nlgn)

    if p < r:
        q = Partition(A, p, r)
        QuickSort(A, p, q-1)
        QuickSort(A, q+1, r)

# PARTITION Θ(n)
def Partition(A, p, r): 

    x = A[r]
    i = p-1
    count = 0

    for j in range(p, r):
        if A[j] == x:
            count += 1
        if A[j] <= x: # change to >= for decreasing order
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i+1], A[r] = A[r], A[i+1]

    return i+1-count//2

# RANDOMIZED-PARTITION
def RandomizedPartition(A, p, r):

    i = random.randint(p,r)
    A[i], A[r] = A[r], A[i]

    return Partition(A,p,r)

# RANDOMIZED-QUICKSORT
def RandomizedQuickSort(A, p, r):

    if p < r:
        q = RandomizedPartition(A,p,r)
        RandomizedQuickSort(A,p,q-1)
        RandomizedQuickSort(A,q+1,r)

# DRIVER
A = [13,19,9,5,12,8,7,4,21,2,6,11]
QuickSort(A,0,len(A)-1)
print(A)
