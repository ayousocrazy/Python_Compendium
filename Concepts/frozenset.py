"""
Frozensets are same as sets but are immutable(unchangeable)
We cannot use pop, add, update, remove, discard methods
It is defined by using the reserved word frozenset()
"""

nums = [x for x in range(1, 21)]
frozen = frozenset(nums)
print(frozen)
print(type(frozen))
"""
Output:
frozenset({1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20})
<class 'frozenset'>
"""

# -------------------------------------------------------------------------------------------------------------------------

frozen1 = frozenset({1, 2, 3})
frozen2 = frozenset({3, 4, 5})

frozen3 = frozen1.union(frozen2)
print(frozen3)
"""
Output:
frozenset({1, 2, 3, 4, 5})

You can create a new frozenset and use methods like difference, intersection, ...
"""