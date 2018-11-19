'''
Matrix multiply
'''
# -*- coding: utf-8 -*-
# __author__ = 'xzq'

class Matrix_Error(Exception):
    def __str__(self):
        return 'Please input right matrix'

class Matrix():
    def __init__(self,rows,cols,*args):
        data_length = len(args)
        try:
            if rows*cols != data_length:
                raise Matrix_Error
            else:
                self.rows = rows
                self.cols = cols
                for i in range(0,self.rows):
                    self.__dict__[i] = list(args[i*self.cols: (i+1)*cols])
        except Matrix_Error as e:
            print(e)

    def __setitem__(self, row, col, value):
        self.__dict__[row][col]

    def __getitem__(self, item):
        return  self.__dict__[item]

    def __call__(self, *args, **kwargs):
        for i in range(0,self.rows):
            for j in range(0,self.cols):
                print(self[i][j], end=' ')
                if j == self.cols - 1:
                    print()

'''
Based on the linaer algebra:  c_ij = \sum\limits_{k=1}^{n}a_ik* b_kj
                              time-complexity: O(n^3)
'''
def Matrix_Multiply(A,B):
    empty_data = [0]*(A.rows*B.cols)
    C = Matrix(A.rows, B.cols, *empty_data)
    for i in range(0, A.rows):
        for j in range(0, B.cols):
            for k in range(0, A.cols):
                C[i][j] = C[i][j] + A[i][k]*B[k][j]
    return C
