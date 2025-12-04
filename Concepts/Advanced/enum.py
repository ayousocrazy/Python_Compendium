from enum import Enum

class Constant(Enum):
    PI = 3.14159265358979323846264338327950288419716939937510
    E = 2.71828182845904523536028747135266249775724709369996

"""
Enum stands for Enumeration

Enum is a class where
- Each member has a name and a constant value
- Members are unique, constant, and fixed
- You use them when you want a set of predefined, unchangeable identifiers
"""

print(Constant.PI)
print(Constant.PI.value) # to get the value you have to set .value
print(Constant.E.value)
print(Constant["PI"])
print(Constant(2.71828182845904523536028747135266249775724709369996))

"""
Output:
Constant.PI
3.141592653589793
2.718281828459045
Constant.PI
Constant.E
"""

Constant.PI.value = 4 # this will raise an error
# Enums are immutable
# Enum members cannot have their .value changed
print(Constant.PI.value)