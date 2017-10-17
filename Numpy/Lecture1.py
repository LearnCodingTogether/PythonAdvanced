#we talk about arrays in this lecture
import numpy
n=numpy.arange(27)
#1D array
print(n)

#2D-Array
print(n.reshape(3,9))

#3D-Array
print(n.reshape(3,3,3))

#Convert List as array
List1=[[10,2,3],[1,2,23,345]]
m=numpy.asarray(List1)
print(type(m))
print(m)
