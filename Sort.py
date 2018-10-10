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
            j = j - 1
        A[j+1] = key
    return A

# recursive
def Insert(A, r):
    key = A[r]
    i = r - 1
    while i >=0 and A[i] > key:
        A[i+1] = A[i]
        i = i - 1
    A[i+1] = key

def InsertSortRecursive(A, r):
    if r > 0:
        InsertSortRecursive(A, r - 1)
        Insert(A, r)
    return A

'''
Selection Sort
'''
def SelectionSort(A):
    for i in range(0, len(A)-1):
        smallest = i
        for j in range(i+1,len(A)):
            if A[j] < A[smallest]:
                smallest = j
        A[i], A[smallest] = A[smallest], A[i]
    return A

'''
Merge Sort
'''
def MergeInf(A,p,q,r):
    Inf = float('Inf')
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

def Merge(A, p, q, r):
    L = A[p:q+1]
    R = A[q+1:r+1]
    n1 = len(L)
    n2 = len(R)
    i = j = 0
    k = p
    while i < n1 and j < n2:
        if L[i] < R[j]:
            A[k] = L[i]
            i = i + 1
            k = k + 1
        else:
            A[k] = R[j]
            j = j + 1
            k = k + 1
    if i == n1:
        A[k:r+1] = R[j:n2]
    else:
        A[k:r+1] = L[i:n1]

def MergeSort(A, p, r):
    if p < r:
        q = math.floor((p+r)/2)
        MergeSort(A, p, q)
        MergeSort(A, q+1, r)
        # MergeInf(A, p, q, r)
        Merge(A, p, q, r)
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
Search
'''
# linear Search
def LinearSearch(A, v, p, r):
    for i in range(p, r+1):
        if A[i] == v:
            return i
    return 'Nil'

# binary Search
def BinarySearch(A, v, p, r):
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
def BinarySearchRecursive(A, v, p, r):
    if p > r:
        return 'Nil'
    q = math.floor((p+r)/2)
    if A[q] == v:
        return q
    elif A[q] < v:
        return BinarySearchRecursive(A, v, q+1, r)
    else:
        return BinarySearchRecursive(A, v, p, q-1)

# test
A = [5,2,4,7,1,3,2,6]
A_new = Merge_Insert_Sort(A, 0, 7, 3)
print(A_new)