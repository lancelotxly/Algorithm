'''
Find the max subarray from a array list:
      e.g Input A = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
          Output  the max subarray from 7 to 10, and the sum is 43

Modules requirements: import math
'''
# -*- coding: utf-8 -*-
# __author__ = 'xzq'
import math

'''
Divide and conquer method: the max_subarray must be in
                           A_left[low,...,mid] or A_right[mid+1,...,high] or A_cross[i,...j] (where low<=i<=j<=high)
                           time-complexity O(nlgn)
'''
def Find_Max_Crossing_Subarray(A,p,q,r):
    Inf = float('Inf')
    low, high = None, None
    sum = 0
    left_sum, right_sum = -Inf, -Inf
    for i in range(q,p-1,-1):
        sum = sum + A[i]
        if sum > left_sum:
            left_sum = sum
            low = i
    sum = 0
    for j in range(q+1,r+1):
        sum = sum + A[j]
        if sum > right_sum:
            right_sum = sum
            high = j
    return low, high, left_sum + right_sum

def Find_Max_Subarray(A,low,high):
    if low == high:
        return low, high, A[low]
    mid = math.floor((low + high) / 2)
    left_low, left_high, left_sum = Find_Max_Subarray(A, low, mid)
    right_low, right_high, right_sum = Find_Max_Subarray(A, mid + 1, high)
    cross_low, cross_high, cross_sum = Find_Max_Crossing_Subarray(A, low, mid, high)

    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_low, left_high, left_sum
    if right_sum >= left_sum and right_sum >= cross_sum:
        return right_low, right_high, right_sum
    if cross_sum >= left_sum and cross_sum >= right_sum:
        return cross_low, cross_high, cross_sum

'''
Brute force algorithm: select the max subarray from all combination of the array
                       time-complexity: O(n^2)
'''
def Brute_Force_Algorithm(A):
    A_length = len(A)
    low, high = None, None
    max = A[0]
    for i in range(0,A_length):
        sum_temp = 0
        for j in range(i,A_length):
            sum_temp += A[j]
            if sum_temp > max:
                max = sum_temp
                low = i
                high = j
    return low, high, max

'''
Linear time max subarray: if max_subarray 'A_sub' of A[1,..,j] is known, the max_subarray of A[1,...,j,j+1] must be 
                          'A_sub' or some subarray A[i,..j,j+1] (1<=i<=j+1)
                          time-complexity: O(n)  
'''
def Linear_Time_Max_Subarray(A):
    A_length = len(A)
    low, high = None,None
    low_temp = 0
    sum_temp = 0
    max = A[0]
    for i in range(0,A_length):
        sum_temp += A[i]
        if sum_temp > max:
            max = sum_temp
            low = low_temp
            high = i
        if sum_temp < 0:
            sum_temp = 0
            low_temp = i + 1
    return low, high, max

# # #test
# A = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
# l, r, s = Linear_Time_Max_Subarray(A)
# print(l,r,s)
