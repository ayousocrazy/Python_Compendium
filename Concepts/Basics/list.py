"""
Lists are collection of multiple values under a single name defined using [] sign
Lists are ordered and are mutable(changeable)
"""

prime_nums = [2, 3, 5, 7, 11, 13, 17, 19, 23]
print(prime_nums)
print(type(prime_nums))
"""
Output:
[2, 3, 5, 7, 11, 13, 17, 19, 23]
<class 'list'>
"""

result = ["Arsenal", 91, "Man United", 99]
print(result)
# You can create list of different data types as well
"""
Output:
["Arsenal", 91, "Man United", 99]
"""

# -------------------------------------------------------------------------------------------------------------------------

print(prime_nums[2:])
print(prime_nums[-1::-1])
"""
Output:
[5, 7, 11, 13, 17, 19, 23]
[23, 19, 17, 13, 11, 7, 5, 3, 2]
The index value of list works similar to string
Read from string.py
"""

# -------------------------------------------------------------------------------------------------------------------------

even_nums = [2, 4, 6, 8, 11, 13, 14, 15]
print(even_nums)
even_nums[4:] = [10, 12, 14, 16, 18]
print(even_nums)
# Lists are changeable
"""
Output:
[2, 4, 6, 8, 11, 13, 14, 15]
[2, 4, 6, 8, 10, 12, 14, 16, 18]
"""

# -------------------------------------------------------------------------------------------------------------------------

# There are several list list methods that help in modifying list 
palindrome = [22,88, 88, 121, 8228, 9559, 32423, 88, 66]
print(palindrome)
palindrome.append(643346)
print(palindrome)
# adds value to the last index 
palindrome.insert(2, 454)
print(palindrome)
# adds value based on specified index (index, value)
palindrome2 = [1221, 13431, 4556554]
palindrome.extend(palindrome2)
print(palindrome)
# extends the list by adding values of another list 
count = palindrome.count(88)
print(count)
# counts number of specified value stored in list
removed = palindrome.pop(3)
print(removed)
print(palindrome)
# removes value based on index and also returns the removed value 
removed = palindrome.pop()
print(removed)
print(palindrome)
# if index is not specified it removes from the last index 
removed = palindrome.remove(22)
print(removed)
print(palindrome)
# removes value based on the value specified and does not return the removed value 
del palindrome[3: 6]
print(palindrome)
# removes multiple value based on index 
palindrome.sort()
print(palindrome)
# sorts the values in the list 
palindrome.reverse()
print(palindrome)
# reverse sorts the values in the list 

"""
Output:
[22, 88, 88, 121, 8228, 9559, 32423, 88, 66]
[22, 88, 88, 121, 8228, 9559, 32423, 88, 66, 643346]
[22, 88, 454, 88, 121, 8228, 9559, 32423, 88, 66, 643346]
[22, 88, 454, 88, 121, 8228, 9559, 32423, 88, 66, 643346, 1221, 13431, 4556554]
3
88
[22, 88, 454, 121, 8228, 9559, 32423, 88, 66, 643346, 1221, 13431, 4556554]
4556554
[22, 88, 454, 121, 8228, 9559, 32423, 88, 66, 643346, 1221, 13431]
None
[88, 454, 121, 8228, 9559, 32423, 88, 66, 643346, 1221, 13431]
[88, 454, 121, 88, 66, 643346, 1221, 13431]
[66, 88, 88, 121, 454, 1221, 13431, 643346]
[643346, 13431, 1221, 454, 121, 88, 88, 66]
"""

del palindrome
# print(palindrome)
# removes the entire thing and now palindrome is not defined and raises an error

# -------------------------------------------------------------------------------------------------------------------------

odd_nums = [x for x in range(1,30) if x%2 != 0]
print(odd_nums)
# we can loop to create lists this is called list comprehension

nums = [x for x in range(1,30)]
print(nums)
even_nums = [x for x in nums if x%2 == 0]
print(even_nums)

fruits = ["Apple", "Banana", "Mango", "Orange", "Kiwi", "Tomato", "Papaya", "Cherry", "Fig", "Melon"]
print(fruits)
specific_fruits = [x for x in fruits if "a" in x or "A" in x]
print(specific_fruits)

"""
Output:
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
['Apple', 'Banana', 'Mango', 'Orange', 'Kiwi', 'Tomato', 'Papaya', 'Cherry', 'Fig', 'Melon']
['Apple', 'Banana', 'Mango', 'Orange', 'Tomato', 'Papaya']
"""

# -------------------------------------------------------------------------------------------------------------------------

for x in specific_fruits:
    print(x)
# we can also loop the list 
"""
Output:
Apple
Banana
Mango
Orange
Tomato
Papaya
"""

# -------------------------------------------------------------------------------------------------------------------------

# There are build-in functions like min, max, sum we can use
print(even_nums)
print(max(even_nums))
print(min(even_nums))
print(sum(even_nums))

"""
Output:
28
2
210
"""