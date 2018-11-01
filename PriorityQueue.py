'''
Priority queue: inherit from Heap.py
                operation include:  Heap_Maximum()  # get the maximum key value
                                    Heap_Extract_Max()  # pop a maximum key value, and when heapsize < 1, return 'underflow error'
                                    Heap_Insert_key(v)     # insert 'v' into the heap
                                    Heap_Increase_key(x,k)  # increase q[x] to 'k'


'''
from Heap import Heap
Inf = float('Inf')

class HeapError(Exception):
    def Heap_underflow(self):
        print('heap underflow')

    def Heap_samller_than_current_key(self,k):
        print('%s is smaller than current key' % k)

    def Heap_greater_than_current_key(self,k):
        print('%s is greater than current key' % k)

class Priority_Queue_Max(Heap):
    def __init__(self,*args):
        super().__init__(*args)
        self.Build_Max_Heap()

    def Heap_Maximum(self):
        return self[0]

    def Heap_Extract_Max(self):
        try:
            if self.heapsize < 1:
                raise HeapError
            max = self[0]
            self[0] = self[self.heapsize - 1]
            self.heapsize = self.heapsize - 1
            self.Max_Heapify(0)
            return max
        except HeapError as e:
            e.Heap_underflow()

    def Heap_Increase_Key(self,i,k):
        try:
            if k < self[i]:
                raise HeapError
            self[i] = k
            while i > 0 and self[self.Parent(i)] < self[i]:
                self[i], self[self.Parent(i)] = self[self.Parent(i)], self[i]
                i = self.Parent(i)
        except HeapError as e:
            e.Heap_samller_than_current_key(k)

    def Max_Heap_Insert(self,key):
        self.heapsize = self.heapsize + 1
        self[self.heapsize - 1] = - Inf
        self.Heap_Increase_Key(self.heapsize - 1, key)

    def Max_Heap_Delete(self,key):
        self[key] = self[self.heapsize - 1]
        self.heapsize = self.heapsize - 1
        self.Max_Heapify(key)

class Priority_Queue_Min(Heap):
    def __init__(self,*args):
        super().__init__(*args)
        self.Build_Min_Heapify()

    def Heap_Minimum(self):
        return self[0]

    def Heap_Extract_Min(self):
        try:
            if self.heapsize < 1:
                raise HeapError
            min = self[0]
            self[0] = self[self.heapsize - 1]
            self.heapsize = self.heapsize - 1
            self.Min_Heapify(0)
            return min
        except HeapError as e:
            e.Heap_underflow()

    def Heap_Decreas_key(self,i,key):
        try:
            if key > self[i]:
                raise HeapError
            self[i] = key
            while i > 0 and self[self.Parent(i)] > self[i]:
                self[i], self[self.Parent(i)] = self[self.Parent(i)], self[i]
                i = self.Parent(i)
        except HeapError as e:
            e.Heap_greater_than_current_key()

    def Min_Heap_Insert(self,key):
        self.heapsize = self.heapsize + 1
        self[self.heapsize - 1] = Inf
        self.Heap_Decreas_key(self.heapsize - 1, key)

    def Min_Heap_Delete(self,key):
        self[key] = self[self.heapsize-1]
        self.heapsize = self.heapsize - 1
        self.Min_Heapify(key)
# test
A = [16,14,10,8,7,9,3,2,4,1]
q = Priority_Queue_Min(*A)
q.Min_Heap_Insert(-1)
q()
print()
q.Min_Heap_Delete(0)
q()