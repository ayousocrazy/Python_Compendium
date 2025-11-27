"""
Tuples are similar as lists but defined using () sign and tuples are immutable(unchangaeable)
"""

result = ("Arsenal", 91, "Man United", 99)
print(result)
print(type(result))
"""
Output:
('Arsenal', 91, 'Man United', 99)
<class 'tuple'>
"""

# -------------------------------------------------------------------------------------------------------------------------

prime_nums = (2, 3, 5, 7, 11, 13, 17, 19, 23)
print(prime_nums[2::1])
print(prime_nums[-1::-1])
"""
Output:
(5, 7, 11, 13, 17, 19, 23)
(23, 19, 17, 13, 11, 7, 5, 3, 2)

Tuples are ordered and we can access it using index number
"""

# -------------------------------------------------------------------------------------------------------------------------

even_nums = (2, 4, 6, 8, 11, 13, 14, 15)
print(even_nums)
# even_nums[4:] = (10, 12, 14, 16, 18)
# print(even_nums)
# this will raise an error as tuple are not changeable

# instead you can do 
copy = list(even_nums)
copy[4:] = [10, 12, 14, 16, 18]
even_nums = tuple(copy)
print(even_nums)

# or 

even_nums = (2, 4, 6, 8)
copy = (10, 12, 14, 16, 18)
even_nums += copy
print(even_nums)

# -------------------------------------------------------------------------------------------------------------------------

palindrome = (22, 88, 88, 121, 8228, 9559, 32423, 88, 66)
print(palindrome.count(88))
# counts the number of times the specified value appears in the tuple
print(palindrome.index(88))
# returns the index of the FIRST occurrence of the value
print(palindrome.index(88, 3))
# starts dearching from 3
"""
Output:
3
1
7
"""

# -------------------------------------------------------------------------------------------------------------------------

fruits = ("Apple", "Banana", "Mango", "Orange", "Kiwi", "Tomato", "Papaya", "Cherry", "Fig", "Melon")
print(fruits)

specified_fruits = tuple(x for x in fruits if "a" in x or "A" in x)
print(specified_fruits)

for x in specified_fruits:
    print(x)

specified_fruits = (x for x in fruits if "a" in x or "A" in x) # this line create a generator instead of a tuple
print(specified_fruits)

"""
Output:
('Apple', 'Banana', 'Mango', 'Orange', 'Kiwi', 'Tomato', 'Papaya', 'Cherry', 'Fig', 'Melon')
('Apple', 'Banana', 'Mango', 'Orange', 'Tomato', 'Papaya')
Apple
Banana
Mango
Orange
Tomato
Papaya
<generator object <genexpr> at 0x0000021AB55835E0>
"""

# -------------------------------------------------------------------------------------------------------------------------

# You can unpack a tuple
odd_nums = tuple(x for x in range(1, 20) if x%2 != 0)
print(odd_nums)

a, *b, c = odd_nums
print(a, b, c)

"""
Output:
1 [3, 5, 7, 9, 11, 13, 15, 17] 19

While unpacking a tuple, adding * before a variable name collects the remaining values into a list
You can use only one * variable in the unpacking
There must be enough elements to fill the non-star variables
"""
# -------------------------------------------------------------------------------------------------------------------------

print(max(palindrome))
print(min(palindrome))
print(sum(palindrome))

# tuple does support these inbuilt functions