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
        print('%s smaller than current key' % k)

class Priority_Queue(Heap):
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

    def Heap_Insert(self,key):
        self.heapsize = self.heapsize + 1
        self[self.heapsize - 1] = - Inf
        self.Heap_Increase_Key(self.heapsize - 1, key)

# test
A = [16,14,10,8,7,9,3,2,4,1]
q = Priority_Queue(*A)
q.Heap_Insert(17)
q()