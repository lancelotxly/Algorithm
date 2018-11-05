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

'''
# -*- coding: utf-8 -*-
# __author__ = 'xzq'
import math
Inf = float('Inf')

'''
Insertion sort
'''
# normal
def InsertionSort(A):
    for i in range(1,len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j = j -1
        A[j+1] = key
    return A

# recursive
def Insert(A,r):
    key = A[r]
    i = r - 1
    while i >=0 and A[i] > key:
        A[i+1] = A[i]
        i = i - 1
    A[i+1] = key

def InsertionSortRecursive(A,r):
    if r > 0:
        InsertionSortRecursive(A,r-1)
        Insert(A,r)

'''
Selection Sort
'''
def SelectionSort(A):
    for i in range(0, len(A)-1):
        smallest = i
        for j in range(i+1, len(A)):
            if A[smallest] > A[j]:
                smallest = j
        A[i], A[smallest] = A[smallest], A[i]

'''
Merge Sort
'''
def MergeInf(A,p,q,r):
    L = A[p:q+1]
    R = A[q+1:r+1]
    L.append(Inf)
    R.append(Inf)
    i = j = 0
    for k in range(p,r+1):
        if L[i] < R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1

def Merge(A,p,q,r):
    L = A[p:q+1]
    R = A[q+1:r+1]
    nL = len(L)
    nR = len(R)
    i = j = 0
    k = p
    while i < nL and j < nR:
        if L[i] < R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1
        k = k + 1

    if i == nL:
        A[k:r+1] = R[j:nR]
    else:
        A[k:r+1] = L[i:nL]

def MergeSort(A,p,r):
    if p < r:
        q = math.floor((p+r)/2)
        MergeSort(A,p,q)
        MergeSort(A,q+1,r)
        # MergeInf(A,p,q,r)
        Merge(A,p,q,r)
    return A

'''
Merge and Insertion combine
'''
def Insert_K(A, p, r):
    for i in range(p+1,r+1):
        key = A[i]
        j = i -1
        while j >=0 and A[j] > key:
            A[j+1] = A[j]
            j = j - 1
        A[j+1] = key

def Merge_Insert_Sort(A, p, r, k):
    if (r-p+1) > k:
        q = math.floor((p+r)/2)
        Merge_Insert_Sort(A, p, q, k)
        Merge_Insert_Sort(A, q+1, r, k)
        Insert_K(A, p, r)
    return A

'''
Bubble Sort
'''
def BubbleSort(A):
    for i in range(0,len(A)-1):
       for j in range(len(A)-1,i,-1):
           if A[j] < A[j-1]:
               A[j], A[j-1] = A[j-1], A[j]

'''
HeapSort: Base on Max-Heap
          time-complexity: O(nlgn)
'''
from Heap import Heap
def HeapSort(A):
    h = Heap(*A)
    h.Build_Max_Heap()
    i = h.heapsize - 1
    while i >= 1:
        h[0], h[i] = h[i], h[0]
        h.heapsize = h.heapsize - 1
        h.Max_Heapify(0)
        i = i - 1
    return h

def HeapSort(A):
    h = Heap(*A)
    h.Build_Max_Heap()
    i = h.heapsize - 1
    while i >= 1:
        h[0], h[i] = h[i], h[0]
        h.heapsize = h.heapsize - 1
        h.Max_Heapify(0)
        i = i - 1
'''
Quick Sort: time-complexity: O(nlgn)
'''
def Partition(A,p,r):
    x = A[r]
    i = p - 1
    for j in range(p,r):
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1
def Quick_Sort(A,p,r):
    if p < r:
        q = Partition(A,p,r)
        Quick_Sort(A,p,q-1)
        Quick_Sort(A,q+1,r)
    return A

# Random case
from random import randint
def Randomized_Partition(A,p,r):
    i = randint(p,r)
    A[r], A[i] = A[i], A[r]
    return Partition(A,p,r)

def Randmized_Quick_Sort(A,p,r):
    if p < r:
        q = Randomized_Partition(A,p,r)
        Randmized_Quick_Sort(A,p,q-1)
        Randmized_Quick_Sort(A,q+1,r)

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
    B = [0]*A_length
    C = [0]*(max_A+1)
    for i in range(0,A_length):
        C[A[i]] = C[A[i]] + 1
    for i in range(1,len(C)):
        C[i] = C[i] + C[i-1]
    for i in range(A_length-1,-1,-1):
        B[C[A[i]]-1] = A[i]
        C[A[i]] = C[A[i]] - 1
    return B

def Count_Interval_Number(A,max_A,a,b):
    A_length = len(A)
    B = [0]*A_length
    C = [0]*(max_A+1)
    for i in range(0,A_length):
        C[A[i]] = C[A[i]] + 1
    for i in range(1,len(C)):
        C[i] = C[i] + C[i-1]
    return C[b] - C[a-1]

'''
Radix Sort: it's a advanced edition of Count-Sort,
            1. we divide the data which for to sort into digits
            2. then use Count-Sort in each digits from low to high
            
            Input: >=0, maximum of the array
            Output: increasing order array
            time-complexity: O(d(n+k))
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
    A_digit = []
    def Preprocess():
        for i in range(0,A_length):
            number = [i,]
            for digit in range(max_digit-1,-1,-1):
                digit_data = (A[i] // 10**digit) % 10
                number.append(digit_data)
            A_digit.append(tuple(number))
    Preprocess()

    digit_i = max_digit
    index = list(range(0,A_length))
    B = [0]*A_length
    while digit_i >= 1:
        C = [0]*10
        digit_data = [tuple([x, A_digit[x][digit_i]]) for x in index]
        for i in range(0,A_length):
             C[digit_data[i][1]] = C[digit_data[i][1]] + 1
        for i in range(1,10):
             C[i] = C[i] + C[i-1]
        for i in range(A_length-1,-1,-1):
             B[C[digit_data[i][1]]-1] = digit_data[i]
             C[digit_data[i][1]] = C[digit_data[i][1]] - 1
        index = [B[i][0] for i in range(0,A_length)]
        digit_i = digit_i - 1
    A_new = [A[x] for x in index]
    return A_new

'''
Bucket Sort: we assume the elements of input array 'A' are Uniform distributed.
             1. we design a bucket according to the maximum of 'A'. Specially, there are sqrt(maximum)+1 buckets
             2. we use insertion sort at each buckets and then combine these buckets as the buckets' order
             
             Input : >=0 integer
             Output: increasing order array
             time-complexity: O(n)       
'''
from math import floor, sqrt,ceil
def Bucket_Sort(A,max_A):
    A_length = len(A)
    n = ceil(sqrt(max_A)) + 1
    B = [0]*n
    B_new = []
    for i in range(0,A_length):
        B[floor(A[i]/n)] = []
    for i in range(0,A_length):
        B[floor(A[i]/n)].append(A[i])
    for i in range(0,A_length):
        B[floor(A[i]/n)] = InsertionSort(B[floor(A[i]/n)])
    for i in range(0,n):
        if isinstance(B[i],list):
             B_new.extend(B[i])
    return B_new



