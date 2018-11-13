'''
Priority queue: inherit from Heap.py
                operation include:  get_PQueue_MaxKey()  # get the maximum key value, time-complexity: O(1)

                                    pop_PQueue_MaxKey()  # pop a maximum key value, and when heapsize < 1, return 'underflow error', time-complexity: O(lgn)
                                    insert_PQueue_NewKey(new_key)     # insert 'v' into the heap, time-complexity: O(lgn)

                                    increase_PQueue_NewKey(i,new_key)  # increase PQ[i] to 'new_key', time-complexity: O(lgn)
                                    decrease_PQueue_to_Newkey(i,new_key)

                                    search_PQueue_key(key)   # return the order of the key
                                    delete_PQueue_ith(i)     # delete the ith key
                                    delete_PQueue_Key(key)   # delete the key


'''
from DataStructure.Heap import Heap

class PQ_Error(Exception):
    def PQ_Underflow(self):
        return 'Priority queue underflow'

    def PQ_Overflow(self):
        return 'Priority queue overflow'

    def PQ_Smaller_NewKey(self,new_key,current_key):
        return 'the new key %d is smaller than the current key %d' % (new_key, current_key)

    def PQ_Greater_Newkey(self,new_key,current_key):
        return 'the new key %d is greater than the current key %d' % (new_key, current_key)

    def PQ_Key_not_found(self,key):
        return 'the key %d is not found' % key

# Maximum priority queue
class Maximum_Priority_Queue(Heap):
    def __init__(self,*args):
        super().__init__(*args)
        self.max_heapsize = self.heapsize
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

    def increase_PQueue_to_NewKey(self,i,new_key):
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

    def decrease_PQueue_to_Newkey(self,i,new_key):
        try:
            if self[i] < new_key:
                raise PQ_Error
            else:
                self[i] = new_key
                self.Max_Heapify(i)
        except PQ_Error as e:
            print(e.PQ_Greater_Newkey(new_key,self[i]))

    def insert_PQueue_NewKey(self,new_key,autoincrease=True):
        try:
            if autoincrease == False:
                raise PQ_Error
            else:
                Inf = float('Inf')
                self.heapsize = self.heapsize + 1
                self.max_heapsize = self.heapsize
                self[self.heapsize-1] = -Inf
                self.increase_PQueue_to_NewKey(self.heapsize-1,new_key)
        except PQ_Error as e:
            print(e.PQ_Overflow())

    def delete_PQueue_ith(self,i):
        self[i] = self[self.heapsize-1]
        self.heapsize = self.heapsize - 1
        self.Max_Heapify(i)

    def search_PQueue_Key(self,key):
        try:
            for i in range(0,self.heapsize):
                if self[i] == key:
                    return i
            if i == self.heapsize:
                raise PQ_Error
        except PQ_Error as e:
            print(e.PQ_Key_not_found(key))

    def delte_PQueue_Key(self,key):
        i = self.search_PQueue_Key(key)
        self.delete_PQueue_ith(i)

# Minimum priority queue
class Minimum_Priority_Queue(Heap):
    def __init__(self,*args):
        super().__init__(*args)
        self.max_heapsize = self.heapsize
        self.Build_Min_Heap()

    def get_PQueue_MinKey(self):
        return self[0]

    def pop_PQueue_MinKey(self):
        try:
            if self.heapsize < 1:
                raise PQ_Error
            else:
                max_key = self[0]
                self[0] = self[self.heapsize-1]
                self.heapsize = self.heapsize - 1
                self.Min_Heapify(0)
                return max_key
        except PQ_Error as e:
            print(e.PQ_Underflow())

    def increase_PQueue_to_NewKey(self, i, new_key):
        try:
            if new_key < self[i]:
                raise PQ_Error
            else:
                self[i] = new_key
                self.Min_Heapify(i)
        except PQ_Error as e:
            print(e.PQ_Smaller_NewKey(new_key, self[i]))

    def decrease_PQueue_to_Newkey(self,i,new_key):
        try:
            if self[i] < new_key:
                raise PQ_Error
            else:
                self[i] = new_key
                while i > 0 and self[self.Parent(i)] > self[i]:
                    self[i], self[self.Parent(i)] = self[self.Parent(i)], self[i]
                    i = self.Parent(i)
        except PQ_Error as e:
            print(e.PQ_Greater_Newkey(new_key,self[i]))

    def insert_PQueue_NewKey(self,new_key,autoincrease=True):
        try:
            if autoincrease == False:
                raise PQ_Error
            else:
                Inf = float('Inf')
                self.heapsize = self.heapsize + 1
                self.max_heapsize = self.heapsize
                self[self.heapsize-1] = Inf
                self.decrease_PQueue_to_Newkey(self.heapsize-1,new_key)
        except PQ_Error as e:
            print(e.PQ_Overflow())

    def delete_PQueue_ith(self,i):
        self[i] = self[self.heapsize-1]
        self.heapsize = self.heapsize - 1
        self.Min_Heapify(i)

    def search_PQueue_Key(self,key):
        try:
            for i in range(0,self.heapsize):
                if self[i] == key:
                    return i
            if i == self.heapsize:
                raise PQ_Error
        except PQ_Error as e:
            print(e.PQ_Key_not_found(key))

    def delte_PQueue_Key(self,key):
        i = self.search_PQueue_Key(key)
        self.delete_PQueue_ith(i)
# test
A = [4,1,3,2,16,9,10,14,8,7]
PQ = Minimum_Priority_Queue(*A)
PQ()
PQ.insert_PQueue_NewKey(0)
PQ()
PQ.delete_PQueue_ith(0)
PQ()