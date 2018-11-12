'''
random. random()  # [0,1) float
        randint(a,b) # [a,b] int
        randrange(stop) # [0,stop) int
        choice(seq)  # select one from the seq
        uniform(a,b) # generate a number satisfying uniform distribute in [a,b]
        expovariate(lambda) # generate a number satisfying exponential distribute
        gauss(mu,sigma) # generate a number satisfying Gaussian distribute
        lognormvariate(mu,sigma) # generate a number satisfying lognormal distribute
'''
'''
Random(a,b):  input: a,b
              output: a random number in [a,b]
              
              method: 1. recode the number in [a,b] with binary, according to random.randin(0,1)
                      2. save the binary code which represents the number in an array A
                      3. rebuild the number based on the binary code, if the rebuild number in [a,b] then output
                         or not replay 1.2
'''
from functools import reduce
from random import randint
from math import floor, log2, ceil

def RandomRange(a,b):
    digit = floor(log2(b-a+1))
    data = []
    def binary2int(x,y):
        return 2*x+y
    while True:
        for i in range(0,digit):
            data.append(randint(0,1))
        delta = reduce(binary2int, data)
        number = a + delta
        if number >= a and number <= b:
            return number
