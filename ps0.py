# Problem Set #0: Powers and Logarithms using Numpy

#Import Numpy for math functions
import numpy as numpy

#Store numbers as floats
x = int(input("Enter number x: "))
y = int(input("Enter number y: "))
#Print results to screen
print("X**y =  " + str(numpy.power(x,y)))
print("log(x) = " + str(int(numpy.log2(x))))
