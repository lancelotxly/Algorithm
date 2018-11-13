'''
tree: connection, no loop, no vector graph
degree of a node:  equal the child nodes of the node
depth of a node: the distance of the root to the node
height of the tree: the maximum of the depth

Binary tree:
    full Binary tree: not exist the node with the degree equal 1, except the leaf nodes
    complete Binary tree: all depth of the leaf nodes are same, and all inner nodes with degree equal 2
                          For a complete tree, the height = log_k^n
                                               the leaf nodes in degree 2 = k^h
                                               inner nodes = (k^h-1)/(k-1)

                          For complete binary tree: the inner nodes = 2^h-1
                                                    the leaf nodes = 2^h
                                                    thus, we obtain the left(or right)-child tree = leaf/2
                                                          and the maximum of the child tree are (2/3)n
'''
'''
Heap: For a Heap of n nodes, n = 2^m-1+k, where m-1 layer complete tree, and the mth layer has k nodes
                            thus, the height of the Heap equal floor(lgn)
      the leaf nodes are floor(n/2)+1, floor(n/2)+2,...n
      the root nodes are 1,..floor(n/2)

      functions: Max_Heapify() and Min_Heapify(), time-complexity: O(lgn)
                 Build_Max_Heap() and Build_Min_Heap(), time-complexity: O(n)
'''
from math import floor

class Heap():
    def __init__(self,*args):
        self.heapsize = len(args)
        for i in range(0,self.heapsize):
            self[i] = args[i]

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __getitem__(self, item):
        return self.__dict__[item]

    def __call__(self, *args, **kwargs):
        for i in range(0,self.heapsize):
            print(self[i],end=' ')
        print()

    def LeftChild(self,i):
        return 2*i+1

    def RightChild(self,i):
        return 2*(i+1)

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

    def Min_Heapify(self,i):
        leftchild = self.LeftChild(i)
        rightchild = self.RightChild(i)
        if leftchild < self.heapsize and self[leftchild] < self[i]:
            smallest = leftchild
        else:
            smallest = i
        if rightchild < self.heapsize and self[rightchild] < self[smallest]:
            smallest = rightchild
        if smallest != i:
            self[i], self[smallest] = self[smallest], self[i]
            self.Min_Heapify(smallest)

    def Build_Max_Heap(self):
        i = floor(self.heapsize/2)
        while i >= 0:
            self.Max_Heapify(i)
            i = i - 1

    def Build_Min_Heap(self):
        i = floor(self.heapsize/2)
        while i >= 0:
            self.Min_Heapify(i)
            i = i - 1

# # test
