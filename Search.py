'''
Search methods, include
      1. LinearSearch(A,v)  from a array 'A' select a variable 'v', time-complexity: O(n)
      2. BinarySearch(A,v,p,r) or BinarySearchRecursive(A,v,p,r) from a order(where increasing order) select a variable, time-complexity: O(lgn)
      3. Select the ith order statistic: from a array select the ith smallest number
                                         1) Based on Selection Sort, time complexity: O(nlgn)

Modules requirements: import math
'''
import math

def LinearSearch(A,v):
    A_length = len(A)
    for i in range(0,A_length):
        if A[i] == v:
            return i
    return 'Nil'

# # binary Search, the input must ordered array, time-complexity: O(lgn)
def Binary_Seach(A,p,r,v):
    while p <= r:
        q = math.floor((p+r)/2)
        if A[q] == v:
            return q
        elif A[q] < v:
            p = q + 1
        else:
            r = q - 1
    return 'Nil'

# binary Search recursive
def Binary_Search_Recursive(A,p,r,v):
    if p > r:
        return 'Nil'
    q = math.floor((p+r)/2)
    if A[q] == v:
        return q
    elif A[q] < v:
        return Binary_Search_Recursive(A,q+1,r,v)
    else:
        return Binary_Search_Recursive(A,p,q-1,v)

'''
Select the ith order statistic: 
           Input: Array and i
           Output: x, there are i-1 numbers in the Array which are all smaller than x
           time-complexity: O(nlgn)
'''
import Sort
def Select_Base_on_SelectionSort(A,i):
    A_new = Sort.MergeSort(A,0,len(A)-1)
    return A_new[i-1]

'''
Randomized Selection: Based on Quick Sort Partition, but only iteration at one side\
                      1. if A_length =1 , return the A[p] or A[r] as the ith number
                      2. Partition the array, and divide the array into A[p,..q-1] and A[q+1,..r] two subarrays
                      3. Count the order of the key as k, if  ith == kth, return A[q]
                      4. if ith < kth, iteration at A[p,..q-1] subarray
                      5. if ith > kth, iteration at A[q+1,..r] subarray
                      time-complexity: O(n)
                      worst-case: O(n^2) we always find out the maximum as the key to divide the subarray..
'''
from Sort import Randomized_Partition
def Randomized_Selection(A,p,r,i):
    if p == r:
        return A[p]
    q = Randomized_Partition(A,p,r)
    k = q-p+1
    if i == k:
        return A[q]
    elif i < k:
        return Randomized_Selection(A,p,q-1,i)
    else:
        return Randomized_Selection(A,q+1,r,i-k)

# iterative edition
def Iterative_Randomized_Selection(A,p,r,i):
    while p < r:
        q = Randomized_Partition(A,p,r)
        k = q-p+1
        if i == k:
            return A[q]
        elif i < k:
            r = q - 1
        else:
            p = q + 1
            i = i - k
    return A[p]


'''

'''