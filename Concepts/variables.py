"""
Variables are names that refer to values stored in memory
There are memory space where we can store values and variables act as access point to that memory unit
"""

num = 100
# Here num is a variable that is storing integer.
print(num)
"""
Output:
100
"""

num2 = 10.24
# num2 is also a variable storing floating point value
print(num2)
"""
Output:
10.24
"""

word = "Ayousocrazy"
# word is a variable carrying string value also called a string varriable
# String are collection of character and character is a single alphanumeric(A to Z, a to z and 0 to 9) as well as special symbols 
print(word)
"""
Output:
Ayousocrazy
"""


# You can check the type of variable using type(variable)
number, sigma =  67, "male"

print (type(number), type(sigma))
"""
Output:
<class 'int'> <class 'str'>
"""
# the variable type is in class because everything in python is an object and 67 is an instance(like child) of class int


word = "replaced :)"
# the program runs from top to bottom and the value of variables can also change
print(word)
"""
Output:
replaced :)
"""
# the variable word previously had value "Ayousocrazy" when defined again the value changes to "replaced :)"

word = 2
print(word)
"""
Output:
2
"""
# you can also replace the type of value 


"""
You can also delete the value of a variable using del
"""
password = "BadDog:("
del password
print(password)
# Now we cannot access "BadDog:(" because it has been deleted
# Will return password is not defined


# Imp: variable doesn't hold the actual value. it holds the memory reference of the value


"""
You can define a variable by assigning value to that variable name
And you cannot use a variable that is not defined
"""
# print (abc)
# This variable is not defined so will return an error of not being defined

"""
You can solve this error by defining the variable before using it
"""
abc = "Atanosoft Berry Computer"
print(abc)


"""
Variable names must start with alphabet or special character "_"
Variable can have numbers but not at the beginning of the name
Variable also cannot be reserved words
Reserved words are words like print, is, if, ... that triggers a function
"""

print = "print"
# This does not return error but now you cannot use print() as you could above as now print is a string not a function
print(abc)
# print(abc) does not work as print has been over written i.e. now Python interpreter thinks this print is a variable name and nothing else