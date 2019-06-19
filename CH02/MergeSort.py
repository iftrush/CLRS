def Merge(A, p, q ,r):

    n1 = q - p + 1
    n2 = r - q
    L = [None for i in range(n1 + 1)]
    R = [None for i in range(n2 + 1)]
    for i in range(0, n1):
        L[i] = A[p + i]
    for j in range(0, n2):
        R[j] = A[q + j + 1]
    L[n1] = 10**10
    R[n2] = 10**10
    i = 0
    j = 0
    for k in range(p, r + 1):
        if(L[i] <= R[j]):
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j] 
            j += 1

def MergeSort(A, p ,r):
    
    if p < r:
        q = (p + r)//2
        MergeSort(A, p, q)
        MergeSort(A, q + 1, r)
        Merge(A, p, q, r)


# DRIVER
Array = [0,1,3,-3,9,2]
MergeSort(Array, 0, len(Array)-1)
print(Array)



