"""
Generators are easier way of creating iterators automatically
"""

def generator(n):
    num1 = 0
    num2 = 1
    num3 = 1
    while n > 0:
        tri = num1 + num2 + num3
        yield num1 # yield returns generator, it returns one value at a time
        num1 = num2
        num2 = num3
        num3 = tri
        n -=1

g1 = generator(10)
print(g1)
print(next(g1))
print(next(g1))

for i in g1:
    print(i)

"""
Output:
<generator object generator at 0x000002161D685380>
0
1
1
2
4
7
13
24
44
81

This is one way of creating generator using function
"""

# -------------------------------------------------------------------------------------------------------------------------

g2 = (x for x in range(25) if x % 5 == 0)
print(g2)
print(g2.__next__())
print(g2.__next__())
for i in g2:
    print(i)

"""
Output:
<generator object <genexpr> at 0x0000013C05E135E0>
0
5
10
15
20

This is another way of creating generator using (expression for iterator)
"""

# -------------------------------------------------------------------------------------------------------------------------

g3 = map(lambda x: x*x*x, range(6))
print(g3)
print(g3.__next__())
for i in g3:
    print(i)
g4 = filter(lambda x: str(x) == str(x)[::-1] and x >= 10, range(50))
print(g4)
print(g4.__next__())
for i in g4:
    print(i)
g5 = zip(range(1, 6), range(5, 0, -1))
print(g5)
print(g5.__next__())
for i in g5:
    print(i)

"""
Output:
<map object at 0x000001D175F26D70>
0
1
8
27
64
125
<filter object at 0x000001D175F26DA0>
11
22
33
44
<zip object at 0x000001D175F4F6C0>
(1, 5)
(2, 4)
(3, 3)
(4, 2)
(5, 1)

These built in functions also return generator
"""

# -------------------------------------------------------------------------------------------------------------------------

def gen():
    yield from "Ayousocrazy"

g6 = gen()
print(g6)
print(g6.__next__())
for i in g6:
    print(i)

"""
Output:
<generator object gen at 0x000002967E58CE80>
A
y
o
u
s
o
c
r
a
z
y

Using yield from also generates generator
But Instead of generating values yourself you hand over control to another iterable
"""