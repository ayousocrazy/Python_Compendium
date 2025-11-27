"""
Sets are arrays but are unordered(indexing doesnot work) and mutable(changeable)
Sets doesnot hold repeating value; it enters repeated values only once
Sets can be defined using {} sign
"""

prime_nums = {2, 3, 5, 7, 11, 13, 19, 17, 23}
print(prime_nums)
print(type(prime_nums))
"""
Output:
{unordered version of prime_nums}
<class 'set'>

Sets uses hash tables to store so the order is not fixed
As it uses hash so checking values in sets is faster than lists and tuples
"""

# -------------------------------------------------------------------------------------------------------------------------

even_nums = {2, 4, 6, 8, 10, 12, 14, 16, 18}
print(even_nums)
even_nums.add(20)
print(even_nums)
# adds new values
random_nums = [33, 42, 1, 56]
even_nums.update(random_nums)
print(even_nums)
# updates new array into sets

even_nums = {2, 4, 6, 8, 10, 12, 14, 16, 18}
odd_nums = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19}
palindrome = {22, 88, 88, 121, 8228, 9559, 32423, 88, 66}

integers = even_nums.union(odd_nums, palindrome)
print(integers)
# you can also do integers = even_nums | odd_nums | palindrome

even_nums.remove(14)
print(even_nums)
# removes the value from set but if the value is not present in the set it raises an error
even_nums.discard(18)
print(even_nums)
# removes the value from set but if the value is not present in the set it does not raise an error
even_nums.pop()
print(even_nums)
# removes a value at random 
even_nums.clear()
print(even_nums)
# clears all the values from the set 
del even_nums 
# print(even_nums)
# raises an error as it deletes the entire thing

"""
there are other methods like
even_nums.difference (-)
even_nums.intersection(&)
even_nums.symmetric_difference(^)
"""

# -------------------------------------------------------------------------------------------------------------------------

fruits = {"Apple", "Banana", "Mango", "Orange", "Kiwi", "Tomato", "Papaya", "Cherry", "Fig", "Melon"}

print(set(x for x in fruits if "a" in x or "A" in x))
# You can also loop through a set 
"""
Output:
{'Orange', 'Tomato', 'Papaya', 'Banana', 'Apple', 'Mango'}
"""