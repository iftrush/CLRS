def AddBinary(A, B):

    C = [None for i in range(len(A) + 1)]
    i = carry = 0
    for i in range(len(A)):
        C[i] = (A[i] + B[i] + carry) % 2
        carry = (A[i] + B[i] + carry) // 2
    C[i+1] = carry

    return C

# DRIVER    
A = [1, 1, 1]
B = [1, 1, 1]
print(AddBinary(A, B))
