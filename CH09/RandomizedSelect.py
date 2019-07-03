import random

# PARTITION Θ(n)
def Partition(A, p, r): 

    x = A[r]
    i = p-1

    for j in range(p, r):
        if A[j] <= x: # change to >= for decreasing order
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i+1], A[r] = A[r], A[i+1]

    return i+1

# RANDOMIZED-PARTITION
def RandomizedPartition(A, p, r):

    i = random.randint(p,r)
    A[i], A[r] = A[r], A[i]

    return Partition(A,p,r)

# RANDOMIZED-SELECT Returns the ith smallest element of the array A[p...r]
def RandomizedSelect(A, p, r, i):

    if p == r: 
        return A[p]
    q = RandomizedPartition(A, p, r)
    k = q - p + 1 # the number k of elements in the subarray A[p...q], pivot q included
    if i == k: # the pivot value is the answer
        return A[q]
    elif i < k: # the desired element lies on the low side of the partition, i smallest of A[p...q-1]
        return RandomizedSelect(A, p, q-1, i)
    else:       # the desired element lies on the high side of the partition, (i-k) smallest of A[q+1...k] 
        return RandomizedSelect(A, q+1, r, i-k)

# RANDOMIZED-SELECT-ITERATIVE
def RandomizedSelectIter(A, p, r, i):

    while(True):
        if p == r:
            return A[p]
        q = RandomizedPartition(A, p, r)
        k = q - p + 1
        if i == k:
            return A[q]
        elif i < k:
            r = q - 1
        else:
            p = q + 1
            i -= k

    
# DRIVER
A = [i for i in range(100)]
MIN = RandomizedSelect(A, 0, len(A)-1, 50)
print(MIN)
MIN = RandomizedSelectIter(A, 0, len(A)-1, 50)
print(MIN)
