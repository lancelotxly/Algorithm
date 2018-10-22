'''
Matrix multiply
'''
# -*- coding: utf-8 -*-
# __author__ = 'xzq'
class Matrix_Define_Error(Exception):
    def __str__(self):
        return 'Please input right square matrix'

class Matrix():
    def __init__(self,n, *args, zero=False):
        try:
            if len(args) != n*n and zero == False:
                raise Matrix_Define_Error
            elif zero == False:
                for i in range(0,n):
                      self.__dict__[i] = list(args[i*n:i*n+n])
            else:
                pass
        except Matrix_Define_Error as e:
            print(e)

    def __getitem__(self, item):
        return self.__dict__[item]

    def __setitem__(self, key, key2, value):
        self.__dict__[key][key2] = value

    def __call__(self, *args, **kwargs):
        for i in range(0,len(self.__dict__)):
            for j in range(0,len(self.__dict__[0])):
                print(self[i][j],end=' ')
                if j == len(self.__dict__[0])-1:
                    print()
#test
m = Matrix(3,1,2,3,4,5,6,7,8,9)
m[0][0]=-1
m()


def Square_Matrix_Multiply(A,B):
    n = len(A[0])


Square_Matrix_Multiply(m,m)
