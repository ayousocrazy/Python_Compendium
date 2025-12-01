from functools import reduce
func = lambda a, b, c : f"{a} {b} {c} : {a+b} {b+c} {a+c}"

result = func(9, 11, 14)
print(result)
"""
Output:
9 11 14 : 20 25 23

A lambda function is a quick way to create a small, one-line function without using def.
It can take multiple inputs but can only return a single expression.
"""

print((lambda a, b, c : f"{a} {b} {c} : {a*b} {b*c} {a*c}")(11, 9, 2))
# You can also use inline lambda function

# -------------------------------------------------------------------------------------------------------------------------

fruits = {'apples': 22, 'mangoes': 30, 'grapes': 15, 'bananas': 36, 'plums': 40, 'oranges': 5}

print(sorted_fruits := sorted(fruits, key = lambda x : fruits[x]))

lst = [1223221, 434, 6677, 89898, 806, 456, 760, 3445, 3664663, 778877, 787, 303, 404]

palindrome = list(filter(lambda n : str(n) == str(n)[::-1], lst))
print(palindrome)
non_palindrome = list(filter(lambda n : str(n) != str(n)[::-1], lst))
print(non_palindrome)
make_palindrome = list(map(lambda n : int((s := str(n)) + s[-2::-1]), non_palindrome))
print(make_palindrome)
print(sum_non_palindrome := reduce(lambda a, b : a + b, non_palindrome))

"""
Output:
['plums', 'bananas', 'mangoes', 'apples', 'grapes', 'oranges']
[1223221, 434, 89898, 3664663, 778877, 787, 303, 404]
[6677, 806, 456, 760, 3445]
[6677766, 80608, 45654, 76067, 3445443]
12144

These are some built-in function where lambda function can be used
"""

# -------------------------------------------------------------------------------------------------------------------------

def func(n):
    return lambda a : f"{a} * {n} = {a*n}"

result = func(9)
print(result)
print(result(11))
# You can also use lambda function as returning value of a function
# The print(result(11)) works using the inline lambda method 