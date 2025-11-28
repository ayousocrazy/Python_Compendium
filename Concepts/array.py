from array import *
from numpy import array as arr, linspace, arange, ones, zeros, logspace, geomspace, concatenate

"""
Array in python are collection of different values of same data type
It is defined using the array function of array module or using numpy
We also need to define the data type of array
"""

nums = array('i', [2, 4, 5, 6, 8, 10])
print(nums)
print(type(nums))
print(nums.buffer_info())

"""
Output:
array('i', [2, 4, 5, 6, 8, 10])
<class 'array.array'>
(2004137779376, 6)

buffer_info returns the memory address and number of data in the array
"""

# -------------------------------------------------------------------------------------------------------------------------

nums.reverse()
print(nums)
print(nums[2])
nums.index(10)
print(nums)
nums.append(12)
print(nums)
num = array('i', [14, 16])
nums.extend(num)
print(nums)
print(nums.pop())
print(nums)

"""
Output:
array('i', [10, 8, 6, 5, 4, 2])
6
array('i', [10, 8, 6, 5, 4, 2])
array('i', [10, 8, 6, 5, 4, 2, 12])
array('i', [10, 8, 6, 5, 4, 2, 12, 14, 16])
16
array('i', [10, 8, 6, 5, 4, 2, 12, 14])

You can carry all methods like list
"""

# Additionally
print(nums.typecode)
# this gives the type of data in the array 

"""
the type of data must be explicitly defined
i for signed integer
I for unsigned integer
l for large signed integer
L for large unsigned integer
u for unicode(string)
f for floating point
d for decimal(longer floating point)
"""

# -------------------------------------------------------------------------------------------------------------------------

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

prime = array(nums.typecode, (x for x in range(2, 100) if is_prime(x)))
print(prime)
# You can also use array comprehension to create array 

# -------------------------------------------------------------------------------------------------------------------------

numpy_array = arr([2, 4, 6, 8, 10])
print(numpy_array)
print(numpy_array.dtype)
# Create array using array function of numpy
# Dont have to explicitly declare the data type 
numpy_array = arr([2, 4, 6, 8, 10], float)
print(numpy_array.dtype)

"""
Output:
[ 2  4  6  8 10]
int64
float64
"""

numpy_arr = linspace(1, 50, 10)
print(numpy_arr)
# This will divide 1-50 into 10 parts and create an array
# It includes the extreme value 
# This has start, stop and parts 
"""
Output:
[ 1. 6.44444444 11.88888889 17.33333333 22.77777778 28.22222222 33.66666667 39.11111111 44.55555556 50.]
"""

numpy_arr = geomspace(1, 1000, 4)
print(numpy_arr)
# This geometricallt divides the parts in 4 parts
"""
Output:
[   1.   10.  100. 1000.]
"""

numpy_arr = logspace(1, 40, 5)
print(numpy_arr)
# This is same as linspace but It starts from 10log base 1 to 10log base 40 and divides to 5 parts
"""
Output:
[1.00000000e+01 5.62341325e+10 3.16227766e+20 1.77827941e+30 1.00000000e+40]
"""

numpy_arr = arange(1, 50, 3)
print(numpy_arr)
# This is same as range but create array of it 
# this has a start, stop and steps 
"""
Output:
[ 1  4  7 10 13 16 19 22 25 28 31 34 37 40 43 46 49]
"""

numpy_arr = ones(5)
print(numpy_arr)
numpy_arr = zeros(5)
print(numpy_arr)
# This creates array with 5 1s and 5 0s
"""
Output:
[1. 1. 1. 1. 1.]
[0. 0. 0. 0. 0.]
"""

# -------------------------------------------------------------------------------------------------------------------------

example1 = arr([1, 2, 3, 4, 5, 6, 7])
example2 = arr([7, 6, 5, 4, 3, 2, 1])

print(example2 + 4)
print(example1 + example2)
print(concatenate([example1, example2]))
print(sum(example1))
"""
Output:
[11 10  9  8  7  6  5]
[8 8 8 8 8 8 8]
[1 2 3 4 5 6 7 7 6 5 4 3 2 1]
28

You can conduct these operations and more on array 
"""

# -------------------------------------------------------------------------------------------------------------------------

array_ex = arr([11, 22, 33, 44, 55, 66, 77, 88, 99])

array_copy = array_ex
print(id(array_ex))
print(id(array_copy))
print(array_ex)
print(array_copy)
array_ex[0] = 10
print(array_ex)
print(array_copy)
"""
This is called Aliasing as you can modify one using other and both point to same memory address
"""

array_copy = array_ex.view()
print(id(array_ex))
print(id(array_copy))
print(array_ex)
print(array_copy)
array_ex[0] = 11
print(array_ex)
print(array_copy)
"""
This is called shallow copy where you still one modifies with other
"""

array_copy = array_ex.copy()
print(id(array_ex))
print(id(array_copy))
print(array_ex)
print(array_copy)
array_ex[0] = 10
print(array_ex)
print(array_copy)
"""
This is called deep copy
"""