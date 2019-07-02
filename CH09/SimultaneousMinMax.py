# SIMULTANEOUS-MINIMUM-MAXIMUM, Total Number of Comparisons at most 3*(n//2)
def SimultaneousMinMax(A):

    n = len(A)
    i = 0 #index

    if n % 2 == 1:
        MIN = MAX = A[0]
        i = 1
    else:
        if A[1] >= A[0]:
            MAX, MIN = A[1], A[0]
        else:
            MAX, MIN = A[0], A[1]
        i = 2

    while i < n:
        if A[i] >= A[i+1]:
            MAX = max(MAX,A[i])
            MIN = min(MIN,A[i+1])
        else:
            MAX = max(MAX,A[i+1])
            MIN = min(MIN,A[i])
        i += 2
        
    return MAX, MIN


# DRIVER
A = [i for i in range(100)]
MAX, MIN = SimultaneousMinMax(A)
print(MAX, MIN)
