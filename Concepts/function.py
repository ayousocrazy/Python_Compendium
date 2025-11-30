"""
You can call a function from anywhere in your program, and you can call it as many times as you want.
"""

# Function definition 
def add(a, b): # these varaiables are formal arguments
    result = a + b
    return(result)

# function call
print(add(6, 5))  # these varaiables are actual arguments

# -------------------------------------------------------------------------------------------------------------------------

def product(num1, num2, num3):
    print(num1 * num2 * num3)
product(22, 33, 44) # this is called position argument method
product(num2 = 22, num1 = 55, num3 = 66) # this is keyword argumet method

def division(num1, num2 = 4):
    print(num1 / num2)
division(24) # this is called default argument method
division(24, 3) # it overwrites the default value 

def adda(*b):
    s = 0
    print(b)
    for i in b:
        s += i
    print(s)
adda(123, 456, 789) # this is called variable length arguments
# This is used when we don't know the total number of value

def info(name, **kwargs):
    print(f"name: {name}")
    for key, val in kwargs.items():
        print(f"{key}: {val}")
info("Ram Chand", age = 44, profession = "trader", DOB = "12 Jan 1999")
# **  sign converts into dictionary and is used when we need the data key with values

# -------------------------------------------------------------------------------------------------------------------------

def xtra(num):
    print(id(num))
    num = 20
    print(id(num))

a = 10
print(id(a))
xtra(a)
print(a)
print(id(a))
# Here integer, float or string are immutable so when we pass them they are called immutable arguments

def xtra_large(lst):
    lst[0], lst[1], lst[2] = 11, 22, 33
    print(id(lst))

l = [10, 20, 30]
print(l)
print(id(l))
xtra_large(l)
print(l)
print(id(l))
# list is mutable so when we pass lists as argements they are mutable arguments

# -------------------------------------------------------------------------------------------------------------------------

