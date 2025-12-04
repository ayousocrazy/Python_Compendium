"""
You can check the memory address of a variable usind id()
"""

num1 = 7
num2 = 1001
num3 = num2

print(id(num1))
print(id(num2))
print(id(num3))

# this will give the memory location and when we do a = b for two variables the memory location of both variable is same making Python memory efficient

print(id(1001))
print(id(7))
# when a constant is allocated to a variable it also can access the memory address

num1 = 8
print(id(num1))
# when the value changes the memory address also changes

print(id(7))
"""
the memory location of 7 still appears after value of num1 has changed because 
Python pre-allocates and caches small integers (–5 to 256)
"""
print(id("bramhastra"))
"""
string object stored in memory, and Python keeps many string objects alive due to:
string interning, and
the fact that string literals are part of your code constants.
"""