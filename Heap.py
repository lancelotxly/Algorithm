from math import floor
class Heap():
    def __init__(self,*args):
        self.length = self.heapsize = len(args)
        for i in range(0,self.heapsize):
            self[i] = args[i]

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __getitem__(self, item):
        return self.__dict__.get(item)

    def __call__(self, *args, **kwargs):
        for i in range(0,self.length):
            print(self[i], end=' ')

    def LeftChild(self,i):
        return  2*i+1

    def RightChild(self,i):
        return  2*(i+1)

    def Parent(self,i):
        return floor((i-1)/2)

    def Max_Heapify(self,i):
        leftchild = self.LeftChild(i)
        rightchild = self.RightChild(i)
        if leftchild < self.heapsize and self[leftchild] > self[i]:
            largest = leftchild
        else:
            largest = i
        if rightchild < self.heapsize and self[rightchild] > self[largest]:
            largest = rightchild
        if largest != i:
            self[i], self[largest] = self[largest], self[i]
            self.Max_Heapify(largest)

    def Build_Max_Heap(self):
        i = floor(self.heapsize/2)
        while i >= 0:
            self.Max_Heapify(i)
            i = i - 1

