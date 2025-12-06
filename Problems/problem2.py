"""
Custom Range Class
Create a class MyRange(start, end, step=1) that behaves like Python’s built-in range.

Requirements:
-No using Python’s range internally.
-Class must be an iterator (define __iter__ and __next__).
-It must support:
    for x in MyRange(1, 10, 2):
        print(x)
"""

class MyRange:
    def __init__(self, start, end=None, step=1):
        if end is None:
            end = start
            start = 0
        
        self.start = start
        self.end = end
        self.step = step
        self.current = start

        if step == 0:
            raise ValueError("step cannot be 0")

    def __iter__(self):
        return self

    def __next__(self):
        if self.step > 0:
            if self.current >= self.end:
                raise StopIteration
        else:
            if self.current <= self.end:
                raise StopIteration

        val = self.current
        self.current += self.step
        return val


# TESTS
print("Test 1:")
for x in MyRange(1, 10, 2):
    print(x)

print("Test 2:")
for x in MyRange(10, 0, -2):
    print(x)

print("Test 3:")
for x in MyRange(5):
    print(x)