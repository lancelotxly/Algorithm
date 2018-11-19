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

class PQueue_Error(Exception):
    def Underflow(self):
        print('Priority queue is underflow')

    def Overflow(self):
        print('Priority queue is overflow')

    def Key_Not_Found(self,key):
        print('The key (%d) is not found' % key)

    def Smaller_Than_Current_Key(self,new_key,current_key):
        print('The new key (%d) is smaller than the current key (%d)' % (new_key, current_key))

    def Greater_Than_Current_Key(self,new_key,current_key):
        print('The new key (%d) is greater than the current key (%d)' % (new_key, current_key))

class Maximum_Priority_Queue(Heap):
    def __init__(self,*args):
        super().__init__(*args)
        self.Max_heap_size = self.heap_size
        self.Build_Max_Heap()

    def get_MaxKey(self):  # O(1)
        return self[0]

    def pop_MaxKey(self):  # O(lgn)
        try:
            if self.heap_size < 1:
                raise PQueue_Error
            else:
                max_key = self[0]
                self[0], self[self.heap_size - 1] = self[self.heap_size - 1], self[0]
                self.heap_size = self.heap_size - 1
                self.Max_Heapify(0)
                return max_key
        except PQueue_Error as e:
            e.Underflow()

    def increase_Current_Key_to(self,i,new_key): # O(lgn)
        try:
            if new_key < self[i]:
                raise PQueue_Error
            else:
                self[i] = new_key
                while i > 0 and self[self.Parent(i)] < self[i]:
                    self[i], self[self.Parent(i)] = self[self.Parent(i)], self[i]
                    i = self.Parent(i)
        except PQueue_Error as e:
            e.Smaller_Than_Current_Key(new_key, self[i])

    def decend_Current_Key_to(self,i,new_key):  # O(lgn)
        try:
            if new_key > self[i]:
                raise PQueue_Error
            else:
                self[i] = new_key
                self.Max_Heapify(i)
        except PQueue_Error as e:
            e.Greater_Than_Current_Key(new_key,self[i])

    def insert_to_PQueue(self,new_key, auto_increase = True):  # O(lgn)
        Inf = float('Inf')
        try:
            if auto_increase == False and self.Max_heap_size == self.heap_size:
                raise PQueue_Error
            else:
                self.heap_size = self.heap_size + 1
                self.Max_heap_size = self.heap_size
                self[self.heap_size - 1] = -Inf
                self.increase_Current_Key_to(self.heap_size-1,new_key)
        except PQueue_Error as e:
            e.Overflow()

    def search_PQueue(self,key):               # O(n)
        try:
            for i in range(0,self.heap_size):
                if self[i] == key:
                      return i
            raise PQueue_Error
        except PQueue_Error as e:
            e.Key_Not_Found(key)

    def delete_Key_by_Order(self,i):    # O(lgn)
        self[i] = self[self.heap_size - 1]
        self.heap_size = self.heap_size - 1
        self.Max_Heapify(i)

    def delete_Key_by_Value(self,key):   # O(n+lgn)
        i = self.search_PQueue(key)
        if i != None:
            self.delete_Key_by_Order(i)


class Minimum_Priority_Queue(Heap):
    def __init__(self,*args):
        super().__init__(*args)
        self.Max_heap_size = self.heap_size
        self.Build_Min_Heap()

    def get_MinKey(self):
        return self[0]

    def pop_MinKey(self):
        try:
            if self.heap_size < 1:
                raise PQueue_Error
            else:
                min_key = self[0]
                self[0], self[self.heap_size - 1] = self[self.heap_size - 1], self[0]
                self.heap_size = self.heap_size - 1
                self.Min_Heapify(0)
                return min_key
        except PQueue_Error as e:
            e.Underflow()

    def increase_Current_Key_to(self,i,new_key):
        try:
            if new_key < self[i]:
                raise PQueue_Error
            else:
                self[i] = new_key
                self.Min_Heapify(i)
        except PQueue_Error as e:
            e.Smaller_Than_Current_Key(new_key,self[i])

    def decend_Current_Key_to(self,i,new_key):
        try:
            if new_key > self[i]:
                raise PQueue_Error
            else:
                self[i] = new_key
                while i > 0 and self[self.Parent(i)] > self[i]:
                    self[i], self[self.Parent(i)] = self[self.Parent(i)], self[i]
                    i = self.Parent(i)
        except PQueue_Error as e:
            e.Greater_Than_Current_Key(new_key,self[i])

    def insert_to_PQueue(self,new_key, auto_increase = True):
        Inf = float('Inf')
        try:
            if auto_increase == False and self.Max_heap_size == self.heap_size:
                raise PQueue_Error
            else:
                self.heap_size = self.heap_size + 1
                self.Max_heap_size = self.heap_size
                self[self.heap_size-1] = Inf
                self.decend_Current_Key_to(self.heap_size-1,new_key)
        except PQueue_Error as e:
            e.Overflow()

    def search_PQueue(self,key):
        try:
            for i in range(0,self.heap_size):
                if self[i] == key:
                    return i
            raise PQueue_Error
        except PQueue_Error as e:
            e.Key_Not_Found(key)

    def delte_Key_by_Order(self,i):
        self[i] = self[self.heap_size-1]
        self.heap_size = self.heap_size - 1
        self.Min_Heapify(i)

    def delte_Key_by_Value(self,key):
        i = self.search_PQueue(key)
        if i != None:
            self.delte_Key_by_Order(i)

