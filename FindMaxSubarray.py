'''
Find the max subarray from a array list:
      e.g Input A = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
          Output  the max subarray from 7 to 10, and the sum is 43

'''
# -*- coding: utf-8 -*-
# __author__ = 'xzq'
from math import floor
Inf = float('Inf')
'''
Divide and conquer method: the max_subarray must be in
                           A_left[low,...,mid] or A_right[mid+1,...,high] or A_cross[i,...j] (where low<=i<=j<=high)
                           time-complexity O(nlgn)
'''
def Find_Max_Crossing_Subarray(A,low,mid,high):
    left_sum, right_sum = -Inf, -Inf
    max_low, max_high = None, None
    sum = 0
    for i in range(mid,low+1,-1):
        sum = sum + A[i]
        if sum > left_sum:
            left_sum = sum
            max_low = i

    sum = 0
    for i in range(mid+1,high+1):
        sum = sum + A[i]
        if sum > right_sum:
            right_sum = sum
            max_high = i

    return max_low, max_high, left_sum + right_sum

def Find_Max_Subarray(A,low,high):
    if low == high:
        return low, high, A[low]
    else:
        mid = floor((low+high)/2)
        left_low, left_high, left_sum = Find_Max_Subarray(A,low,mid)
        right_low, right_high, right_sum = Find_Max_Subarray(A,mid+1,high)
        cross_low, cross_high, cross_sum = Find_Max_Crossing_Subarray(A, low, mid, high)

    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_low, left_high, left_sum
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return right_low, right_high, right_sum
    else:
        return cross_low, cross_high, cross_sum

'''
Brute force algorithm: select the max subarray from all combination of the array
                       time-complexity: O(n^2)
'''
def Brute_Force_Algorithm(A):
    left, right = None, None
    curSum = 0
    max = A[0]
    for i in range(0,len(A)):
        curSum = 0
        for j in range(i,len(A)):
            curSum = curSum + A[j]
            if curSum > max:
                max = curSum
                left = i
                right = j
    return left, right, max
'''
Linear time max subarray: if max_subarray 'A_sub' of A[1,..,j] is known, the max_subarray of A[1,...,j,j+1] must be 
                          'A_sub' or some subarray A[i,..j,j+1] (1<=i<=j+1)
                          time-complexity: O(n)  
'''
def Linear_Time_Max_Subarray(A):
    max = -Inf
    low, high = None, None
    sum = 0
    low_r = 0
    for i in range(0, len(A)):
        sum = sum + A[i]
        if sum > max:
            max = sum
            low = low_r
            high = i
        if sum < 0:
            sum = 0
            low_r = i + 1
    return low, high, max

#test
A = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
#A = [-5,-3,-4,-8]
l,r,s = Find_Max_Subarray(A,0,len(A)-1)
#l,r,s = Brute_Force_Algorithm(A)
#l, r, s = Linear_Time_Max_Subarray(A)
print(l,r,s)

