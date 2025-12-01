import sys
"""
When a function calls itself it is called recursion function
"""

def aSequence(a, d, num):
    if num <= 1:
        print(a)
    else:
        print(a, end=", ")
        a += d
        num -= 1
        aSequence(a, d, num)

a = int(input("Enter first term: "))
d = int(input("Enter common difference: "))
n = int(input("Enter number of terms: "))

aSequence(a, d, n)
# Using recursion to print Arithemetic Sequence 

# -------------------------------------------------------------------------------------------------------------------------

print(sys.getrecursionlimit())
sys.setrecursionlimit(500)
print(sys.getrecursionlimit())

tn = 0

def gSequence(a, r):
    globals()['tn'] += 1
    print(f"{globals()['tn']}th {a}" , end=", ")
    a *= r
    gSequence(a, r)

a = int(input("Enter first term: "))
r = int(input("Enter common ration: "))

gSequence(a, r)
# The default recursion limit is 1000 and can change it using setrecursionlimit 