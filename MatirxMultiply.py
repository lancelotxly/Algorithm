'''
Matrix multiply
'''
# -*- coding: utf-8 -*-
# __author__ = 'xzq'
class Matrix_Define_Error(Exception):
    def __str__(self):
        return 'Please input right square matrix'

class Matrix():
    def __init__(self,n,list):
        try:
            if len(list) != n*n:
                raise Matrix_Define_Error
            else:
                for i in range(0, n):
                    self.__dict__[i] = list[i*n:i*n+n]
                self.rows = n
        except Matrix_Define_Error as e:
            print(e)

    def __setitem__(self, key1, key2, value):
        self.__dict__[key1][key2] = value

    def __getitem__(self, item):
        return self.__dict__[item]

    def __call__(self, *args, **kwargs):
        for i in range(0,self.rows):
            for j in range(0, self.rows):
                print(self[i][j], end=' ')
                if j == self.rows - 1:
                    print()

#test
# A = list(range(1,10))
# m = Matrix(3,A)
# for i in range(0,3):
#     for j in range(0,3):
#         m[i][j] = 1
# print(m.__dict__)
'''
Based on the linaer algebra:  c_ij = \sum\limits_{k=1}^{n}a_ik* b_kj
                              time-complexity: O(n^3)
'''
def Square_Matrix_Multiply(A,B):
    n = A.rows
    list = [0]*(n*n)    # generate a zero vector
    C = Matrix(n,list)
    for i in range(0,n):
        for j in range(0,n):
            for k in range(0,n):
                C[i][j] = C[i][j] + A[i][k]*B[k][j]
    return C


A = Matrix(3,list(range(1,10)))
A()
print(A[1][0:2])