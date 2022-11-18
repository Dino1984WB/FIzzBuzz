import numpy as np

x = np.arange(1,101) #produce an array of numbers 1 - 100

for i in x: #iterate though array x
    if i % 15 == 0: #if the current iterator, ie position in array, is divisble by 15
        print ("FizzBuzz")
    elif i % 3 == 0: # is divisible by 3
        print("Fizz")
    elif i % 5 == 0: #divisible by 5
        print("Buzz") 
    else:
        print(i)  
