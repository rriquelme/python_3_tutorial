# What is numpy? Numerical Python.
# What does it have? ndarray, efficient multidimensional array, mathematical functions.
# How to use it? the common way is:
import numpy as np

# Generate random data:

random_ndarray = np.random.randn(3,4)
print(random_ndarray)

random_ndarray = np.random.randn(3,4)
print(random_ndarray)

# convert to int:

print(random_ndarray.astype(np.int32))

# List can be converted to ndarray:

L = [ 1,2,3,4,5,6,7,8,9]

print(L)
print(np.array(L))

# or mnultple arrays in a multidementional ndarray:
print(np.array([L,L,L]))

# all arithmetic on nparray are made on each element:
nd_array = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(nd_array)

print(nd_array*2)
print(nd_array+2)
print(nd_array-2)
print(nd_array/2)
print(nd_array>5) # Boolean returns the ndarray of logic result and can be replaced like:
print(nd_array[nd_array>5])

#Slicing -> "same" as Lists

print(nd_array[1,2]) #6
print(nd_array[0,2]) #3
print(nd_array[:,2]) 
print(nd_array[1,:]) 
print(nd_array[1,-1]) 
print(nd_array[1,-1:]) 

# Reshape
print(nd_array.reshape(9,1))
print(nd_array.reshape(1,9))

# Traspose
print(nd_array.T)

# Inner matrix product:
print(np.dot(nd_array,nd_array))

## Could be improved adding more functions... max min sum mean... etc