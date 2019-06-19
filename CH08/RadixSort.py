# COUNTING-SORT based on digits
def CountingSort(A, exp): 
  
    n = len(A) 
    B = [0] * (n) 
    C = [0] * (10) 
  
    for i in range(n):
        index = A[i]//exp
        C[index%10] += 1  #occurrence of digit in ones -> tens -> hundreds

    for i in range(1,10): 
        C[i] += C[i-1] 

    for i in range(n-1, -1, -1):
        index = A[i]//exp
        B[C[index%10] - 1] = A[i]
        C[index%10] -= 1

    for i in range(len(A)): 
        A[i] = B[i] 

# RADIX-SORT
def RadixSort(A): 
  
    MAX = max(A) 
    exp = 1 
    while MAX // exp > 0:
        CountingSort(A,exp) 
        exp *= 10

# DRIVER
A = [ 170, 45, 75, 90, 802, 24, 2, 66]
RadixSort(A)
print(A)