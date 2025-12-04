from numpy import *

arr_dim2 = array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(arr_dim2)
print(arr_dim2.shape)
print(arr_dim2.size)
print(arr_dim2.ndim)
# This is 2 dimensional array 
"""
Output:
[[1 2 3]
 [4 5 6]
 [7 8 9]]
(3, 3)
9
2
"""

arr_dim3 = array([
    [
    [1, 2],
    [2, 3]
    ], 
    [
    [4, 5],
    [5, 6]
    ]
])
print(arr_dim3)
print(arr_dim3.shape)
print(arr_dim3.size)
print(arr_dim3.ndim)
# This is 3 dimensional array 
"""
Output:
[[[1 2]
  [2 3]]

 [[4 5]
  [5 6]]]
(2, 2, 2)
8
3
"""

# -------------------------------------------------------------------------------------------------------------------------

arr_dim1 = arr_dim2.flatten()
print(arr_dim1)
arr_dim1 = arr_dim3.flatten()
print(arr_dim1)
# turn 2 dimenstional array to 1 dimensional
"""
Output:
[1 2 3 4 5 6 7 8 9]
[1 2 2 3 4 5 5 6]
"""

arr = arr_dim1.reshape(4,2)
print(arr)
# Reshape dimension of array 
"""
Output:
[[1 2]
 [2 3]
 [4 5]
 [5 6]]
"""

# -------------------------------------------------------------------------------------------------------------------------

mat = matrix(arr)
print(mat)
print(type(mat))
"""
Output:
[[1 2]
 [2 3]
 [4 5]
 [5 6]]
<class 'numpy.matrix'>
"""

m = matrix('10 20; 20 30; 30 40')
print(m)
m1 = matrix('1 2 3; 4 5 6; 7 8 9')
m2 = matrix('11 22 33; 44 55 66; 77 88 99')
print(m1*m2)
"""
Output:
[[10 20]
 [20 30]
 [30 40]]
[[ 330  396  462]
 [ 726  891 1056]
 [1122 1386 1650]]
"""