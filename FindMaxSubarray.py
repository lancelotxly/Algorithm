import math
Inf = float('Inf')
def Find_Max_Crossig_Subarray(A,low,mid,high):
    left_sum = -Inf
    max_left = max_right = 0
    sum = 0
    for i in range(mid,low+1,-1):
        sum = sum + A[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i

    right_sum = -Inf
    sum = 0
    for i in range(mid+1,high+1,1):
        sum = sum + A[i]
        if sum > right_sum:
            right_sum = sum
            max_right = i
    max_sum = left_sum + right_sum
    return max_left, max_right, max_sum

def Find_Max_Subarray(A, low, high):
    if high == low:
        return low, high, A[low]
    else:
        mid = math.floor((low+high)/2)
        left_low, left_high, left_sum = Find_Max_Subarray(A, low, mid)
        righ_low, right_high, right_sum = Find_Max_Subarray(A, mid+1, high)
        cross_low, cross_high, cross_sum = Find_Max_Crossig_Subarray(A, low, mid, high)

    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_low, left_high, left_sum
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return righ_low, right_high, right_sum
    else:
        return cross_low, cross_high, cross_sum

# test
A = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
l,r,s = Find_Max_Subarray(A,0,len(A)-1)
print(l,r,s)

