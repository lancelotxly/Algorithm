'''
Matrix multiply
'''
# -*- coding: utf-8 -*-
# __author__ = 'xzq'

class MatrixError(Exception):
    def Definition_Error(self):
        return 'Please input right matrix'

class Matrix():
    def __init__(self,data,rows,cols):
        data_lenght = len(data)
        try:
            if data_lenght != rows * cols:
                raise MatrixError
            else:
                self.rows = rows
                self.cols = cols
                for i in range(0,rows):
                    self.__dict__[i] = data[i*cols:(i+1)*cols]
        except MatrixError as e:
            print(e.Definition_Error())

    def __setitem__(self, row, col, value):
        self.__dict__[row][col] = value

    def __getitem__(self, item):
        return self.__dict__[item]

    def __call__(self, *args, **kwargs):
        for i in range(0,self.rows):
            for j in range(0,self.cols):
                print(self[i][j], end=' ')
                if j == self.cols - 1:
                    print()

    def Matrix_Multiply(self,other):
        data = [0] * (self.rows * other.cols)
        C = Matrix(data,self.rows, other.cols)
        for i in range(0,self.rows):
            for j in range(0,other.cols):
                for k in range(0,self.cols):
                    C[i][j] += self[i][k] * other[k][j]
        return C
