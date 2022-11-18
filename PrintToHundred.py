#FizzBuzz problem 1 - print numbers 1 to 100
import numpy as np


#Easy way to solve, with numpy library
x = np.arange(1,101)
print(x)


#this is the answer from fizzbuzz, but while using only builtin functions, it is more convoluted logically in my opinion.
for i in range(1,101):
    print(i)


#KEY: use the high level stuff when possible it was designed to make life easier, no matter if it seems harder at first.