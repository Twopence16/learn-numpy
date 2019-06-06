# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 14:54:20 2018

@author: twope
"""

import numpy as np

'''
1.Create a null vector of size 10
'''


'''
2.Create a null vector of size 10
'''

'''
3.How to find the memory size of any array
'''

'''
4.Create a null vector of size 10 but the fifth value which is 1 
'''
a = np.empty(10)
a[4] = 1
print(a)

'''
5.Create a vector with values ranging from 10 to 49
'''
a = np.arange(10,50)
print(a)

'''
6.Reverse a vector (first element becomes last)
'''
a = np.arange(1,10)
a[-1::-1]

'''
7. Create a 3x3 matrix with values ranging from 0 to 8 
'''
a = np.arange(0,9).reshape(3,3)
print(a)

'''
8.Find indices of non-zero elements from [1,2,0,0,4,0]
'''
np.nonzero([1,2,0,0,4,0])

'''
9.Create a 3x3 identity matrix 
'''
a = np.eye(3)
print(a)

'''
10.Create a 3x3x3 array with random values 
'''
a = np.random.random([3,3,3])
print(a)

'''
11.Create a 10x10 array with random values and find the minimum and maximum values
'''
a = np.random.random([10,10])
np.max(a)
np.min(a)

'''
12.Create a 2d array with 1 on the border and 0 inside
'''
a = np.ones([10,10])
a[1:-1,1:-1] = 0 
print(a)

'''
13.How to add a border (filled with 0's) around an existing array?
'''
#https://docs.scipy.org/doc/numpy/reference/generated/numpy.pad.html
a = np.ones([10,10])
a = np.pad(a,pad_width = 2,mode = 'constant',constant_values = 0)
print(a)
#np.pad 用法,(3,2)指第一个维度,(2,3)指第二个维度
a = np.array([[1,2],[3,4]])
a
np.pad(a,pad_width =((3,2),(2,3)),mode = 'constant',constant_values = 0)

'''
14.Create a 5x5 matrix with values 1,2,3,4 just below the diagonal
'''
a = np.diag([1,2,3,4],k = -1)
print(a)

'''
15.Create a 8x8 matrix and fill it with a checkerboard pattern
'''
a = np.zeros([8,8])
a[0::2,1::2] = 1
a[1::2,0::2] = 1
print(a)

'''
16.Consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th element?
'''
np.unravel_index(100,(6,7,8))

'''
17.Create a checkerboard 8x8 matrix using the tile function
'''
np.tile([[1,0],[0,1]],(4,4))

'''
18.Normalize a 5x5 random matrix
'''
a = np.random.random([5,5])
a = (a-np.mean(a))/np.std(a)

'''
19.Multiply a 5x3 matrix by a 3x2 matrix (real matrix product)
'''
a = np.ones([5,3])
b = np.ones([3,2])
np.dot(a,b)

'''
20. Given a 1D array, negate all elements which are between 3 and 8, in place.
'''
a = np.arange(1,10)
a[(a>3)&(a<8)] *= -1
print(a)
