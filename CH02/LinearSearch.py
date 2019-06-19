def LinearSearch(A, v):

    for i in range(0, len(A)):
        if A[i] == v:
            return i
            
    return False

# DRIVER
A = [1,2,3,4,5]
print(LinearSearch(A, 3))
