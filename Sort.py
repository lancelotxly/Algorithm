'''
Increasing order sort. Input: list
                       Output: list
Including: #1. Sort based on compare, time-complexity must larger than O(nlgn)
           Insertion Sort (O(n^2)), Selection Sort(O(n^2))
           Merge Sort (O(nlgn))
           Merge & Insert combine(O(nk+nlg(n/k)))
           Heap Sort  (O(nlgn))

           #2. Linear time-complexity sort
           Count_Sort  (O(n))  # only for the number are integer and great than zero

           LinearSearch (O(n)), BinarySearch(O(lgn))

Module Requirements: import math
'''
# -*- coding: utf-8 -*-
# __author__ = 'xzq'
import math
'''
Insertion sort : best O(n), worst O(n^2)
'''
# normal
def InsertSort(data,reverse=False):
    data_len = len(data)
    for i in range(1,data_len):
        key = data[i]
        j = i - 1
        if reverse:
            while j >= 0 and data[j] < key:
                data[j+1] = data[j]
                j = j - 1
        else:
            while j >= 0 and data[j] > key:
                data[j+1] = data[j]
                j = j - 1
        data[j+1] = key
    return data

# recursive
def Insert(A,r):
    key = A[r]
    i = r - 1
    while i >= 0 and A[i] > key:
        A[i+1] = A[i]
        i = i - 1
    A[i+1] = key
def InsertSort_Recursive(A,r):
    if r > 0:
        InsertSort_Recursive(A,r-1)
        Insert(A,r)
    return A

'''
Selection Sort: almost O(n^2)
'''
def SelectSort(data,reverse=False):
    data_len = len(data)
    for i in range(0,data_len-1):
        mark = i
        for j in range(i,data_len):
            if reverse:
                if data[j] > data[mark]:
                    mark = j
            else:
                if data[j] < data[mark]:
                    mark = j
        if mark != i:
            data[mark],data[i] = data[i],data[mark]
    return data


'''
Merge Sort: O(nlgn)
'''
def Merge_Inf(A,p,q,r):
    Inf = float('Inf')
    L_array = A[p:q+1]
    R_array = A[q+1:r+1]
    L_array.append(Inf)
    R_array.append(Inf)
    i, j = 0, 0
    for k in range(p,r+1):
        if L_array[i] < R_array[j]:
            A[k] = L_array[i]
            i = i + 1
        else:
            A[k] = R_array[j]
            j = j + 1

def Merge(A,p,q,r):  # No cycle style, because the proceeding include separate and merge, and only the separate recursive has cycle style
    L_array = A[p:q+1]
    R_array = A[q+1:r+1]
    L_length = len(L_array)
    R_length = len(R_array)
    k = p
    i, j = 0, 0
    while i < L_length and j < R_length:
        if L_array[i] < R_array[j]:
            A[k] = L_array[i]
            i = i + 1
        else:
            A[k] = R_array[j]
            j = j + 1
        k = k + 1
    if i == L_length:
        A[k:r+1] = R_array[j:R_length]
    else:
        A[k:r+1] = L_array[i:L_length]

def MergeSort(A,p,r):
    if p < r:
        q = math.floor((p+r)/2)
        MergeSort(A,p,q)
        MergeSort(A,q+1,r)
        # Merge_Inf(A,p,q,r)
        Merge(A,p,q,r)
    return A

'''
Merge and Insertion combine: O(nk+nlg(n/k)) = n/k*(O(k^2)) + O(nlg(n/k))
'''
def Insert_k(A,p,r):
    for i in range(p+1,r+1):
        key = A[i]
        j = i - 1
        while j >= p and A[j] > key:
            A[j+1] = A[j]
            j = j - 1
        A[j+1] = key
def Merge_Insert_Sort(A,p,r,k):
    if r-p+1 > k:
        q = math.floor((p+r)/2)
        Merge_Insert_Sort(A,p,q,k)
        Merge_Insert_Sort(A,q+1,r,k)
        Insert_k(A,p,r)
    return A

'''
Bubble Sort : O(n^2)
'''
def BubbleSort(A):
    A_lenght = len(A)
    for i in range(0,A_lenght-1):
        for j in range(A_lenght-1,i,-1):
            if A[j] < A[j-1]:
                A[j],A[j-1] = A[j-1], A[j]
    return A

'''
HeapSort: Base on Max-Heap
          time-complexity: O(nlgn)
Modules requirements: Heap
'''
from DataStructure.Heap import Heap
def HeapSort(A):
    h = Heap(A)
    h.Build_Max_Heap()
    temp = h.heapsize
    while h.heapsize >= 1:
        h[0], h[h.heapsize-1] = h[h.heapsize-1], h[0]
        h.heapsize = h.heapsize - 1
        h.Max_Heapify(0)
    h.heapsize = temp
    return h

'''
Quick Sort: time-complexity: O(nlgn)
'''
def Quick_Sort(A,p,r):
    def Partition(A,p,r):
        key = A[r]
        i = p - 1
        for j in range(p,r):
            if A[j] < key:
                i = i + 1
                A[i], A[j] = A[j], A[i]
        A[i+1], A[j] = A[j], A[i+1]
        return i + 1
    if p < r:
        q = Partition(A,p,r)
        Quick_Sort(A,p,q-1)
        Quick_Sort(A,q+1,r)
    return A

# Random case
from random import randint
def Randomize_Quick_Sort(A,p,r):
    def Randomize_Partition(A,p,r):
        i = randint(p,r)
        A[i], A[r] = A[r], A[i]
        key = A[r]
        i = p - 1
        for j in range(p,r):
            if A[j] <= key:
                i = i + 1
                A[i], A[j] = A[j], A[i]
        A[i+1], A[r] = A[r], A[i+1]
    if p < r:
        q = Randomize_Partition(A,p,r)
        Randomize_Quick_Sort(A,p,q-1)
        Randomize_Partition(A,q+1,r)
    return A

'''
Count sort: 
          Input: <= 0 and the maximum of array
          Output: increased order array
          time-complexity: O(n) = O(n+k)+O(n)
                                  O(n+k) to count, O(n) to order
Count interval number:
          Input: <=0, the maximum of array, [a,b] to count
          Output: the number of elements fall into [a,b]
          time-complexity: O(n) = O(n+k)+O(1)
                                  O(n+k) to count, O(1) to find out
                           
'''
def Count_Sort(A,max_A):
    A_length = len(A)
    A_new = [0] * A_length
    Count = [0] * (max_A + 1)
    for i in range(0, A_length):
        Count[A[i]] = Count[A[i]] + 1
    for i in range(1, len(Count)):
        Count[i] = Count[i] + Count[i-1]
    for i in range(A_length-1, -1, -1):
        A_new[Count[A[i]] - 1] = A[i]
        Count[A[i]] = Count[A[i]] - 1
    return A_new

def Count_Interval_Number(A,max_A,a,b):
    A_length = len(A)
    Count = [0] * (max_A + 1)
    for i in range(0,A_length):
        Count[A[i]] = Count[A[i]] + 1
    for i in range(1,len(Count)):
        Count[i] = Count[i] + Count[i-1]
    interval_number = Count[b] - Count[a-1]
    if a == 0:
        interval_number = Count[b]
    return interval_number

'''
Radix Sort: it's a advanced edition of Count-Sort,
            1. we divide the data which for to sort into digits
            2. then use Count-Sort in each digits from low to high
            
            Input: >=0, maximum of the array
            Output: increasing order array
            time-complexity: O(d(n+k)), where k = 10
            but the space-complexity is less than corresponding case in Count-Sort.
            
            tips: to locate every data we introduce a tuple about the number and digit, like (number,digit)
            
a//b  # a除以b取商
a**b  # a^b
math.exp(x) # e^x
tuple(list) <--> list(tuple)
str(num)  num to str
'''
def Radix_Sort(A,max_A):
    A_length = len(A)
    max_digit = len(str(max_A))
    A_Digit_Set = []
    def Preprocess():
        for i in range(0, A_length):
            num_vector = [i, ]
            for digit in range(max_digit - 1, -1, -1):
                data = (A[i] // 10 ** digit) % 10
                num_vector.append(data)
            A_Digit_Set.append(tuple(num_vector))
    Preprocess()
    digit_i = max_digit
    index = list(range(0,A_length))
    A_new = [0] * A_length
    while digit_i >= 1:
        Count = [0] * 10
        digit_data_set = [tuple([x, A_Digit_Set[x][digit_i]]) for x in index]
        for i in range(0,A_length):
            Count[digit_data_set[i][1]] = Count[digit_data_set[i][1]] + 1
        for i in range(1,10):
            Count[i] = Count[i] + Count[i-1]
        for i in range(A_length-1,-1,-1):
            A_new[Count[digit_data_set[i][1]] -1] = digit_data_set[i]
            Count[digit_data_set[i][1]] = Count[digit_data_set[i][1]] - 1
        index = [ A_new[i][0] for i in  range(0,A_length)]
        digit_i = digit_i - 1
    A_new = [A[i] for i in index]
    return A_new

'''
Bucket Sort: we assume the elements of input array 'A' are Uniform distributed.
             1. we design a bucket according to the maximum of 'A'. Specially, there are sqrt(maximum)+1 buckets
             2. we use insertion sort at each buckets and then combine these buckets as the buckets' order
             
             Input : >=0 integer
             Output: increasing order array
             time-complexity: O(n)       
'''
from math import floor, ceil, sqrt
def Bucket_Sort(A, max_A):
    A_length = len(A)
    bucket_number = ceil(sqrt(max_A)) + 1
    bucket_storage = [0] * bucket_number
    A_new = []
    for i in range(0,A_length):
        bucket_storage[floor(A[i]/bucket_number)] = []
    for i in range(0,A_length):
        bucket_storage[floor(A[i]/bucket_number)].append(A[i])
    for i in range(0,A_length):
        bucket_storage[floor(A[i]/bucket_number)] = InsertionSort(bucket_storage[floor(A[i]/bucket_number)])
    for i in range(0,bucket_number):
        if isinstance(bucket_storage[i],list):
            A_new.extend(bucket_storage[i])
    return A_new


if __name__ == "__main__":
    A = [1,3,4,6,-9,0]
    A_new = SelectSort(A,reverse=True)
    print(A_new)