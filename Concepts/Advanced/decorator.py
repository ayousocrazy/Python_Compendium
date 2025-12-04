"""
Decorators help add additional feature in a function without changing the code of that func
"""

def make_palindrome(func):
    def inner(num):
        if (s := str(num)) == s[::-1]:
            return func(num)
        else:
            i = len(s) - len(s.rstrip(s[-1]))
            pal = s + s[-i-1::-1]
            return func(int(pal))
    return inner

def function(n):
    return n

new_function = make_palindrome(function)
# this is one way of using decorator by creating a new function 

print(new_function(1221))
print(new_function(122333))
# Decorators here changes the argument of the function 

# -------------------------------------------------------------------------------------------------------------------------

def make_capital(func):
    def inner():
        return func().upper()
    return inner

@make_capital
def txt():
    return "Hello Laura!"
# This is another way of using decorator without creating a new function 

print(txt())
# This takes the return value of function and modifies it 

# -------------------------------------------------------------------------------------------------------------------------

def make_palindrome(n):
    def make_palindrome(func): # you can have the same name of outer or inner function 
    # def decorator(func): makes it less confusing
        def inner(num):
            if n == 1:
                if (s := str(num)) == s[::-1]:
                    return func(num)
                else:
                    i = len(s) - len(s.rstrip(s[-1]))
                    pal = s + s[-i-1::-1]
                    return func(int(pal))
            else:
                return func(num)
        return inner
    return make_palindrome
    #def decorator
    
check = int(input("Enter 1 if you want to make it palindrome: "))
num = int(input("Enter number: "))

@make_palindrome(check)
def function(n):
    return n

# new_function = make_palindrome(check)(function) this can also be done

print(function(num))

# -------------------------------------------------------------------------------------------------------------------------

def make_capital(func):
    def inner():
        return func().upper()
    return inner

def add_text(func):
    def inner():
        return func() + " Have a great day."
    return inner

# You can add multiple decorators for a function 
@make_capital
@add_text
def txt():
    return "Hello Laura!"

# The order of decorator matters as the above acts like make_capital(add_text(txt)) changing the order also changesthe result 
print(txt())

# -------------------------------------------------------------------------------------------------------------------------

def example_function():
    return "hello"

def example_decorator(func):
    def inner():
        return func().upper()
    return inner

@example_decorator
def function_example():
    return "olleh"

print(example_function.__name__)
print(function_example.__name__)
"""
Output:
example_function
inner

the metadata of function gets lost when we use decorator
"""

import functools

def example_function_2():
    return "hello"

def example_decorator_2(func):
    @functools.wraps(func)
    def inner():
        return func().upper()
    return inner

@example_decorator_2
def function_example_2():
    return "olleh"

print(example_function_2.__name__)
print(function_example_2.__name__)
"""
Output:
example_function_2
function_example_2

Using functools.wraps helps to preserve the metadata
"""