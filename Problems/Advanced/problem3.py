"""
Decorator to Cache Function Calls
Write a decorator memoize that stores results of previous function calls.

Example:
    @memoize
    def slow_fib(n):
        if n <= 1: return n
        return slow_fib(n-1) + slow_fib(n-2)
"""

import time

def memoize(func):
    cache = {}

    def decorator(*args):
        if args in cache:         
            return cache[args]
        
        result = func(*args)     
        cache[args] = result   
        return result 
    
    return decorator  

cache = {}

@memoize
def slow_fib(n):
    if n <= 1: return n
    return slow_fib(n-1) + slow_fib(n-2)

def slow_fib2(n):
    if n <= 1: return n
    return slow_fib2(n-1) + slow_fib2(n-2)

# TEST
start = time.time()
print("Without memoize")
print(slow_fib2(40))
print(time.time() - start)
print("-"*30)
start = time.time()
print("With memoize")
print(slow_fib(40))
print(time.time() - start)