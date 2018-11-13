'''
Priority queue: inherit from Heap.py
                operation include:  get_PQueue_MaxKey()  # get the maximum key value, time-complexity: O(1)
                                    pop_PQueue_MaxKey()  # pop a maximum key value, and when heapsize < 1, return 'underflow error', time-complexity: O(lgn)
                                    insert_PQueue_NewKey(new_key)     # insert 'v' into the heap, time-complexity: O(lgn)
                                    increase_PQueue_NewKey(i,new_key)  # increase PQ[i] to 'new_key', time-complexity: O(lgn)


'''
from DataStructure.Heap import Heap

class PQ_Error(Exception):
    def PQ_Underflow(self):
        return 'Priority queue underflow'

    def PQ_Overflow(self):
        return 'Priority queue overflow'

    def PQ_Smaller_NewKey(self,new_key,current_key):
        return 'the new key %d is smaller than the current key %d' % (new_key, current_key)

class Priority_Queue(Heap):
    def __init__(self,*args):
        super().__init__(*args)
        self.max_heapsize = self.heapsize

    def create_Max_PQueue(self):
        self.Build_Max_Heap()

    def get_PQueue_MaxKey(self):
        return self[0]

    def pop_PQueue_MaxKey(self):
        try:
            if self.heapsize < 1:
                raise PQ_Error
            else:
                max_key = self[0]
                self[0] = self[self.heapsize-1]
                self.heapsize = self.heapsize - 1
                self.Max_Heapify(0)
                return max_key
        except PQ_Error as e:
            print(e.PQ_Underflow())

    def increase_PQueue_NewKey(self,i,new_key):
        try:
            if new_key < self[i]:
                raise PQ_Error
            else:
                self[i] = new_key
                while i > 0 and self[self.Parent(i)] < self[i]:
                    self[i], self[self.Parent(i)] = self[self.Parent(i)], self[i]
                    i = self.Parent(i)
        except PQ_Error as e:
            print(e.PQ_Smaller_NewKey(new_key,self[i]))

    def insert_PQueue_NewKey(self,new_key,autoincrease=True):
        try:
            if autoincrease == False:
                raise PQ_Error
            else:
                Inf = float('Inf')
                self.heapsize = self.heapsize + 1
                self[self.heapsize-1] = -Inf
                self.increase_PQueue_NewKey(self.heapsize-1,new_key)
        except PQ_Error as e:
            print(e.PQ_Overflow())


# test
A = [4,1,3,2,16,9,10,14,8,7]
PQ = Priority_Queue(*A)
PQ.create_Max_PQueue()
PQ()
PQ.increase_PQueue_NewKey(9,20)
PQ()