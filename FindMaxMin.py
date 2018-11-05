'''
Find max and min synchronously:
               Input: Array
               Output: maximum and minimum of the array
'''
'''
Find Max adn Min respectively:  time-complexity: O(2n-2)
'''
def FindMaxMin_res(A):
    A_length = len(A)
    max = A[0]
    for i in range(0,A_length):
        if A[i] > max:
            max = A[i]
    min = A[0]
    for i in range(0,A_length):
        if A[i] < min:
            min = A[i]
    return min, max

'''
FindMaxMin_syn:  1. Compare a couple of data, to find the data_maximum and the data_minimum
                 2. Compare between the maximum and the data_maximum
                 3. Compare between the minimum and the data_minimum
                 
                 time-complexity: O(3*floor(n/2))
'''
def FindMaxMin_syn(A):
    def Compare(x,y):
        min, max = x, y
        if min > max:
            min, max = y, x
        return min, max
    A_length = len(A)
    if A_length % 2 == 0:
        start = 2
        min, max = Compare(A[0],A[1])
    else:
        start = 1
        min, max = A[0], A[0]
    for i in range(start,A_length-1):
        A_min, A_max = Compare(A[start],A[start+1])
        min, temp = Compare(A_min, min)
        temp, max = Compare(A_max, max)
    return min, max

A = [9,-1,0,2,5,7,6,4,3,9]
min,max = FindMaxMin_syn(A)
print(min,max)