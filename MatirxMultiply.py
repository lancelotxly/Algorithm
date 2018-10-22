'''
Matrix multiply
'''
# -*- coding: utf-8 -*-
# __author__ = 'xzq'
class Matrix_Define_Error(Exception):
    def __str__(self):
        return 'Please input right square matrix'

class Matrix():
    def __init__(self,n, *args):
        try:
            if len(args) != n*n:
                raise Matrix_Define_Error
            else:
                for i in range(0,n):
                      self.__dict__[i] = args[i*n:i*n+n]

        except Matrix_Define_Error as e:
            print(e)

    def __getitem__(self, item):
        return self.__dict__[item]

    def __setitem__(self, key, value):
        self.__dict__[key] = value
#test
m = Matrix(3,1,2,3,4,5,6,7,8,9)
for i in range(0,3):
    for j in range(0,3):
        print(m[i][j])

def Square_Matrix_Multiply(A,B):
    n = A.rows
    C = Matrix()
