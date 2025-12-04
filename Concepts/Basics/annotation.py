"""
Type annotations describe the expected data type of variables, function parameters, and return values
"""

num: int = int(input("Enter a number: "))
# : <data_typr> is how we use annotation
# num should be an int (but Python will NOT enforce it)

def Cube(n : int) -> int: # : int defines we expect an integer as argument and -> int expects int to be the return value
    return n * n * n

print(Cube(3))

print(Cube(3.33))
# this is a floating point number but it also works

"""
Python does NOT enforce these types at runtime.
They are mainly used for:
- Documentation
- Code readability
- IDE auto-completion
- Static type checking (e.g., mypy)
"""