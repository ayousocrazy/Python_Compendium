"""
Generator: Infinite Fibonacci
Write a generator fibonacci() that yields Fibonacci numbers indefinitely.

Usage:
    fib = fibonacci()
    for _ in range(10):
        print(next(fib))

Requirement:
-Must yield numbers infinitely.
-No lists allowed.
"""

def fibonacci():
    num1 = 0
    num2 = 1
    while True:
        yield num1
        num1, num2 = num2, num1 + num2

fib = fibonacci()

for _ in range(10):
    print(next(fib))