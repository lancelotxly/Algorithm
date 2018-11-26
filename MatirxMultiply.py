'''
Matrix multiply
'''
# -*- coding: utf-8 -*-
# __author__ = 'xzq'

class Matrix_Error(Exception):
    def Matrix_Define_Error(self):
        return 'Please input right matrix'

    def Matrix_Multiply_Error(self):
        return 'Matrix A and B must match'

class Matrix():
    def __init__(self,rows, cols, *args):
        data_length = len(args)
        try:
            if rows * cols != data_length:
                raise Matrix_Error
            else:
                self.rows = rows
                self.cols = cols
                for i in range(0,rows):
                    self.__dict__[i] = list(args[i*cols: (i+1)*cols])
        except Matrix_Error as e:
            print(e.Matrix_Define_Error())

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

    '''
    Based on the linaer algebra:  c_ij = \sum\limits_{k=1}^{n}a_ik* b_kj
                                  time-complexity: O(n^3)
    '''
    def Matrix_Multiply(self,M_A, M_B):
        try:
            if M_A.cols != M_B.rows:
                raise Matrix_Error
            else:
                empty_data = [0] * (M_A.rows * M_B.cols)
                M_C = Matrix(M_A.rows, M_B.cols, *empty_data)
                for i in range(0,M_A.rows):
                    for j in range(0,M_B.cols):
                        for k in range(0,M_A.cols):
                            M_C[i][j] = M_C[i][j] + M_A[i][k] * M_B[k][j]
                return M_C
        except Matrix_Error as e:
            print(e.Matrix_Multiply_Error())
