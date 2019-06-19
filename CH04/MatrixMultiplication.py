def SquareMatrixMultiply(A,B):

    n = len(A)
    C = [[0 for i in range(n)] for i in range(n)]
    for i in range(0,n):
        for j in range(0,n):
            C[i][j] = 0
            for k in range(0,n):
                C[i][j] += A[i][k] * B[k][j]

    return C


def SquareMatrixMultiplyRecursive(A,B):

    n = len(A)
    C = [[0 for i in range(n)] for i in range(n)]
    if n == 1:
        C[0][0] = A[0][0] * B[0][0]
    else:
        A00, A01, A10, A11 = Partition(A)
        B00, B01, B10, B11 = Partition(B)
        C00 = SquareMatrixMultiplyRecursive(A00, B00) + SquareMatrixMultiplyRecursive(A01, B10)
        C01 = SquareMatrixMultiplyRecursive(A00, B01) + SquareMatrixMultiplyRecursive(A01, B11)
        C10 = SquareMatrixMultiplyRecursive(A10, B00) + SquareMatrixMultiplyRecursive(A11, B10)
        C11 = SquareMatrixMultiplyRecursive(A10, B01) + SquareMatrixMultiplyRecursive(A11, B11)
        C = [[0 for i in range(n)] for i in range(n)]
        for i in range(n//2):
            for j in range(n//2):
                C[i][j] = C00[i][j] + C00[i+n//2][j]
                C[i][j+n//2] = C01[i][j] + C01[i+n//2][j]
                C[i+n//2][j] = C10[i][j] + C10[i+n//2][j]
                C[i+n//2][j+n//2] = C11[i][j] + C11[i+n//2][j]
        
    return C

def Partition(A):

    if len(A) % 2 != 0 or len(A[0]) % 2 != 0:
        raise Exception('Odd Matrices Are Not Supported!')
    length = len(A)
    mid = length // 2
    TopLeft = [[A[i][j] for j in range(mid)] for i in range(mid)]
    BotLeft = [[A[i][j] for j in range(mid)] for i in range(mid, length)]
    TopRight = [[A[i][j] for j in range(mid, length)] for i in range(mid)]
    BotRight = [[A[i][j] for j in range(mid, length)] for i in range(mid, length)]

    return TopLeft, TopRight, BotLeft, BotRight



# DRIVER
A = [[1,2], [3,4]]
B = [[5,6], [7,8]]
C = [[1,1,1,1], [2,2,2,2], [3,3,3,3], [4,4,4,4]]
D = [[5,5,5,5], [6,6,6,6], [7,7,7,7], [8,8,8,8]]

print(SquareMatrixMultiply(A,B))


#print(SquareMatrixMultiplyRecursive(A,B))
print(SquareMatrixMultiplyRecursive(C,D))
