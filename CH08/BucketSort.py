from math import floor

# INSERTION-SORT
def InsertionSort(A):
    
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while(i >= 0 and A[i] > key):
            A[i+1] = A[i]
            i -= 1
        A[i+1] = key

# BUCKET-SORT
def BucketSort(A): # 0 <= A[0...n-1] < 1

    n = len(A)
    B = []
    
    for i in range(n):
        B.append([])

    for i in range(n):
        B[floor(n*A[i])].append(A[i])

    for i in range(n):
        InsertionSort(B[i])

    # Concatenate B into A
    k = 0
    for i in B:
        for j in i:
            A[k] = j
            k += 1

# DRIVER
A = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
BucketSort(A)
print(A)
    
