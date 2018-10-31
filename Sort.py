'''
Increasing order sort. Input: list
                       Output: list
Including: Insertion Sort (O(n^2)), Selection Sort(O(n^2))
           Merge Sort (O(nlgn))
           Merge & Insert combine(O(nk+nlg(n/k)))
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

'''
Quick Sort: time-complexity: O(nlgn)
'''
def Partition(A,p,r):
    x = A[r]
    i = p - 1
    for j in range(p,r):
        if A[j] < x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

def Quick_Sort(A,p,r):
    if p < r:
        q = Partition(A,p,r)
        Quick_Sort(A,p,q-1)
        Quick_Sort(A,q+1,r)

# test
A = [4,3,1,0,5,7]
Quick_Sort(A,0,len(A)-1)
print(A)

'''
Search
'''
# linear Search
def LinearSearch(A,v):
    for i in range(0,len(A)):
        if A[i] == v:
            return i
    return 'Nil'

# binary Search
def BinarySearch(A,v,p,r):
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
def BinarySearchRecursive(A,v,p,r):
    if p > r:
        return 'Nil'
    q = math.floor((p+r)/2)
    if A[q] == v:
        return q
    elif A[q] < v:
        return BinarySearchRecursive(A,v,q+1,r)
    else:
        return BinarySearchRecursive(A,v,p,q-1)

