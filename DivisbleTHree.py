#list in console numbers that are multiples of 3, 1-100
#this will probably use modulo, % (returns the remainder from division operation)
import numpy as np

x = np.arange(1,101) #produce an array of numbers 1 - 100


for i in x: #iterate though array x

    fizz = "Fizz"
    if i % 3 == 0: #if the current iterator, ie position in array, is divisble by 3
        print (i) #print out current iterator
        print ("Fizz")
