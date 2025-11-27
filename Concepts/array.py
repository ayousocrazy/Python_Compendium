from array import *

"""
Array in python are collection of different values of same data type
It is defined using the array function of array module
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