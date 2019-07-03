# MEDIAN
def Median(A):

    A.sort()

    return A[len(A)//2]

# SELECT
def Select(A, p, r, i):

    n = len(A)

    if i > 0 and i <= n:

        index = 0
        MED = [0] * ((n+4)//5)

        while index < n//5:
            MED[index] = Median(A[index*5:index*5+5])
            index += 1

        if index*5 < n:
            MED[index] = Median(A[index*5:])
            index += 1

        MEDMED = MED[index-1] if index == 1 else Select(MED, 0, index-1, index//2)
        q = Partition(A, p, r, MEDMED)
        k = q - p + 1

        if k == i:

            return A[q]

        elif i < k:

            return Select(A, p, q-1, i)
            
        else:
            
            return Select(A, q+1, r, i-k)

# PARTITION based on pivot x
def Partition(A, p, r, x): 

    i = p-1

    for j in range(p, r):

        if A[j] <= x: # change to >= for decreasing order
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i+1], A[r] = A[r], A[i+1]

    return i+1

# DRIVER
A = [i for i in range(100)]
print(Select(A, 0, len(A)-1, 2))
