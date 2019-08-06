# -*- coding: utf-8 -*-
import math

__author__ = 'xzq'

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

def SelectSort(data,reverse=False):
    data_len = len(data)
    for i in range(0,data_len-1):
        mark = i
        for j in range(i+1,data_len):
            if reverse:
                if data[j] > data[mark]:
                    mark = j
            else:
                if data[j] < data[mark]:
                    mark = j
        if mark != i:
            data[mark],data[i] = data[i],data[mark]
    return data

def MergeSort(data,start,end,reverse=False):
    def Merge(data,start,end,mid,reverse):
        l_list = data[start:mid+1]
        r_list = data[mid+1:end+1]
        l_len = len(l_list)
        r_len = len(r_list)
        k = start
        i, j = 0, 0
        while i < l_len and j < r_len:
            if reverse:
                if l_list[i] > r_list[j]:
                    data[k] = l_list[i]
                    i = i + 1
                else:
                    data[k] = r_list[j]
                    j = j + 1
            else:
                if l_list[i] < r_list[j]:
                    data[k] = l_list[i]
                    i = i + 1
                else:
                    data[k] = r_list[j]
                    j = j + 1
            k = k + 1

        if i == l_len:
            data[k:end+1] = r_list[j:r_len]
        elif j == r_len:
            data[k:end+1] = l_list[i:l_len]

    def Merge_Int(data,start,end,mid,reverse):
        Inf = float('Inf')
        l_list = data[start:mid+1]
        r_list = data[mid+1:end+1]
        if reverse:
            l_list.append(-Inf)
            r_list.append(-Inf)
        else:
            l_list.append(Inf)
            r_list.append(Inf)
        i,j=0,0
        for k in range(start,end+1):
            if reverse:
                if l_list[i] > r_list[j]:
                    data[k] = l_list[i]
                    i = i + 1
                else:
                    data[k] = r_list[j]
                    j = j + 1
            else:
                if l_list[i] < r_list[j]:
                    data[k] = l_list[i]
                    i = i + 1
                else:
                    data[k] = r_list[j]
                    j = j + 1

    if start < end:
        mid = math.floor((start+end)/2)
        MergeSort(data,start,mid,reverse)
        MergeSort(data,mid+1,end,reverse)
        # Merge(data,start,end,mid,reverse)
        Merge_Int(data,start,end,mid,reverse)
    return data

def InserSort_Recursive(data,end,reverse=False):
    def Insert(data,end,reverse):
        key = data[end]
        i = end - 1
        if reverse:
            while i >= 0 and data[i] < key:
                data[i+1] = data[i]
                i = i - 1
        else:
            while i >= 0 and data[i] > key:
                data[i+1] = data[i]
                i = i - 1
        data[i+1] = key

    if end > 0:
        InserSort_Recursive(data,end-1,reverse)
        Insert(data,end,reverse)
        return data

def MergeInsertSort(data,start,end,K,reverse=False):
    def Insert_K(data,start,end):
        for i in range(start+1,end+1):
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
    if end - start + 1 > K:
        mid = math.floor((start+end)/2)
        MergeInsertSort(data,start,mid,K,reverse)
        MergeInsertSort(data,mid+1,end,K,reverse)
        Insert_K(data,start,end)
    return data

def BubbleSort(data,reverse=False):
    data_len = len(data)
    for i in range(0,data_len-1):
        for j in range(data_len-1,i,-1):
           if (reverse and data[j] > data[j-1]) or (not reverse and data[j] < data[j-1]):
               data[j],data[j-1] = data[j-1],data[j]
    return data

def Find_Max_Subarrary(data,start,end):
    def Find_Max_Crossarrary(data,start,end,mid):
        Inf = float('Inf')
        low, high = None, None
        sum = 0
        left_sum, right_sum = -Inf, -Inf
        for i in range(mid,start-1,-1):
            sum = sum + data[i]
            if sum > left_sum:
                left_sum = sum
                low = i
        sum = 0
        for j in range(mid+1,end+1):
            sum = sum + data[i]
            if sum > right_sum:
                right_sum = sum
                high = j
        return low, high, left_sum + right_sum

    if start == end:
        return start, end, data[start]
    mid = math.floor((start+end)/2)
    left_low,left_high,left_sum = Find_Max_Subarrary(data,start,mid)
    right_low, right_high, right_sum = Find_Max_Subarrary(data,mid+1,end)
    cross_low, cross_high, cross_sum = Find_Max_Crossarrary(data,start,end,mid)

    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_low, left_high, left_sum
    if right_sum >= left_sum and right_sum >= cross_sum:
        return right_low, right_high, right_sum
    if cross_sum >= left_sum and cross_sum >= right_sum:
        return cross_low, cross_high, cross_sum

def Brute_Force_Algorithm(data):
    data_len = len(data)
    low, high = None, None
    MAX = data[0]
    for i in range(0,data_len):
        sum = 0
        for j in range(i,data_len):
            sum += data[j]
            if sum > MAX:
                MAX = sum
                low = i
                high = j
    return low, high, MAX

def Liner_time_Algorithm(data):
    data_len = len(data)
    low, high = None, None
    low_temp = 0
    sum_temp = 0
    max = data[0]
    for i in range(0,data_len):
        sum_temp += data[i]
        if sum_temp > max:
            max = sum_temp
            low = low_temp
            high = i
        if sum_temp < 0:
            low_temp = i + 1
            sum_temp = 0
    return low, high, max

def Find_Subitem(data,num):
    data_len = len(data)
    MergeSort(data,0,data_len-1)
    i = 0
    j = data_len-1
    rep = []
    while i < j:
        temp = data[i] + data[j]
        if temp == num:
            rep.append((data[i],data[j],num))
            i = i + 1
            j = j - 1
        elif temp < num:
            i = i + 1
        elif temp > num:
            j = j - 1

    return rep

def Find_Inversion(data,start,end):
    def Merge_Inversion(data,start,mid,end):
        inv = 0
        L_array = data[start:mid+1]
        R_array = data[mid+1:end+1]
        L_len = len(L_array)
        R_len = len(R_array)
        i,j = 0, 0
        k = start
        while i < L_len and j < R_len:
            if L_array[i] <= R_array[j]:
                data[k] = L_array[i]
                i = i + 1
            else:
                data[k] = R_array[j]
                inv = inv + L_len - i
                j = j + 1
            k = k + 1
        if i == L_len:
            data[k:end+1] = R_array[j:R_len]
        elif j == R_len:
            data[k:end+1] = L_array[i:L_len]
        return inv

    if start < end:
        mid = math.floor((start+end)/2)
        left = Find_Inversion(data,start,mid)
        right = Find_Inversion(data,mid+1,end)
        inv = Merge_Inversion(data,start,mid,end)
        return inv + left + right
    return 0

if __name__ == '__main__':
    A = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
    A  = list(range(100,0,-1))
    rep = Find_Inversion(A,0,len(A)-1)
    print(rep)





