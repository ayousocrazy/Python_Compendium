"""
Build Your Own enumerate
Write a generator my_enumerate(iterable, start=0).

Usage:
    for index, value in my_enumerate(['a','b','c'], 5):
        print(index, value)
"""

def my_enumerate(iterable, start=0):
    current = start
    it = iter(iterable)
    
    while True:
        try:
            value = next(it)
        except StopIteration:
            return
        yield current, value
        current += 1

for index, value in my_enumerate(['a','b','c'], 5):
    print(index, value)