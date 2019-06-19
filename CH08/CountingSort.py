# COUNTING-SORT
def CountingSort(A,B,k): # Elements in A is an integer in the range 0 to k

    C = [0 for i in range(k+1)] # initializes C to all zeros

    for j in range(len(A)):
        C[A[j]] += 1  # C[i] now contains the number of elements equal to i

    for i in range(1,k+1):
        C[i] += C[i-1] 

    for j in range(len(A)-1, -1, -1):
        B[C[A[j]] - 1] = A[j] 
        C[A[j]] -= 1


# DRIVER
A = [6,0,2,0,1,3,4,6,1,3,2]
B = [0 for i in range(len(A))]
k = max(A)
CountingSort(A,B,k)
print(B)
    
