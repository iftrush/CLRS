def FindMaxCrossingSubarray(A, low, mid, high): # cross the mid
    LeftSum = -1000000
    sum = 0
    MaxLeft = mid
    MaxRight = mid + 1
    for i in range(mid, low-1, -1):
        sum = sum + A[i]
        if sum > LeftSum:
            LeftSum = sum
            MaxLeft = i
    RightSum = -1000000
    sum = 0
    for j in range(mid+1, high+1):
        sum += A[j]
        if sum > RightSum:
            RightSum = sum
            MaxRight = j
    return (MaxLeft, MaxRight, LeftSum + RightSum)

def FindMaximumSubArray(A, low, high):
    if low == high:
        return (low, high, A[low]) # base case: only one element
    else:
        mid = int((low + high)/2) 
        (LeftLow, LeftHigh, LeftSum) = FindMaximumSubArray(A, low, mid) 
        (RightLow, RightHigh, RightSum) = FindMaximumSubArray(A, mid+1, high) 
        (CrossLow, CrossHigh, CrossSum) = FindMaxCrossingSubarray(A, low, mid, high) 
        if(LeftSum >= RightSum and LeftSum >= CrossSum):
            return (LeftLow, LeftHigh, LeftSum) 
        elif(RightSum >= LeftSum and RightSum >= CrossSum):
            return (RightLow, RightHigh, RightSum)
        else:
            return (CrossLow, CrossHigh, CrossSum)


# DRIVER
A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
B = [1,2,3,4,5,6,7,8,9,10]
print(FindMaximumSubArray(A, 0, len(A)-1)) ## f(A,0,15)
print(FindMaximumSubArray(B, 0, len(B)-1))
