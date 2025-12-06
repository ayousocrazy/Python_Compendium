"""
Decorator for Debugging
Create a decorator debug that prints:
    Calling <function name> with args <args> and kwargs <kwargs>
    Returned <value>

Apply it like:
    @debug
    def add(a, b):
        return a + b

Requirements:
-Must work for any function.
-Must preserve the original function’s name (functools.wraps not allowed — do manually)
"""

def debug(func):
    def inner(*args, **kwargs):
        print(f"Calling {func.__name__} with args {args} and kwargs {kwargs}")

        result = func(*args, **kwargs)

        print(f"Returned {result}")
        return result

    inner.__name__ = func.__name__
    inner.__doc__ = func.__doc__
    inner.__module__ = func.__module__

    return inner


@debug
def add(a, b):
    return a + b

# TESTS
print("Test:")
print(add(1, 3))