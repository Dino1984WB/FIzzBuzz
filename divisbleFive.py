import numpy as np

x = np.arange(1,101) #produce an array of numbers 1 - 100

for i in x: #iterate though array x
    if i % 5 == 0: #if the current iterator, ie position in array, is divisble by 3
        print (i) #print out current iterator