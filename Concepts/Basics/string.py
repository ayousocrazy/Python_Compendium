string = "Python Compendium"

"""
Strings behave like a list of characters but are IMMUTABLE
IMMUTABLE means that once it is created it's value cannot be changed
Strings have an order and we can access character of string with it's index values
Here string = "Python Compendium" its order goes or it's index value goes like
P = 0
y = 1
t = 2
h = 3
o = 4
n = 5
  = 6
C = 7
o = 8
m = 9
p = 10
e = 11
n = 12
d = 13
i = 14
u = 15
m = 16
Its order starts from 0
"""

print(string[0:10])
# It starts orderly from 0 to 9(one before 10)
"""
Output:
Python Com
"""

print(string[7:])
# Leaving blank after : denoted till the end 
"""
Output:
Compendium
"""

print(string[-17:])
# the string order also works negative
"""
P = -17
y = -16
t = -15
h = -14
o = -13
n = -12
  = -11
C = -10
o = -9
m = -8
p = -7
e = -6
n = -5
d = -4
i = -3
u = -2
m = -1

Output:
Python Compendium
"""

print(string[0:17:2])
"""
Output:
Pto opnim

String slicing works like 
start point:end point:increment step
0:17:2 means starts from 0: till 16th position: and step increases by 2

Step increases by 2 means it will take 0, 2, 4, 6, ....., 16
P = 0
t = 2
o = 4
  = 6
o = 8
p = 10
n = 12
i = 14
m = 16
"""

print(string[-1::-1])
"""
Output:
muidnepmoC nohtyP

Starts from -1 and the step is -1 so -1, -2, -3, ......
"""

# -------------------------------------------------------------------------------------------------------------------------

string[0:6] = "Javascript"
print(string)
# This will raise a error as strings are immutable

new_string = "Javascript" + string[6:]
string = "".join([x for x in new_string])
print(string)
# You can do this instead
"""
Output:
Javascript Compendium
"""

# -------------------------------------------------------------------------------------------------------------------------

word1 = "Bread"
word2 = "and"
word3 = "Butter"

final_word = word1 + word2 + word3
print(final_word)
"""
Output:
BreadandButter
"""
del final_word
final_word = word1 + " " + word2 + " " + word3
print(final_word)
"""
Output:
Bread and Butter
"""

# -------------------------------------------------------------------------------------------------------------------------

example_str1 = "Arsenal"
example_str2 = "Man United"

score1 = 91
score2 = 99

result = example_str1 + ":" + score1 + " & " + example_str2 + ":" + score2
print(result)
# This will raise an error as we cannot combine string and integer

# We use formated string instead
result = f"{example_str1}:{score1} & {example_str2}:{score2}"
print(result)
"""
Formatted string works by adding f before the "" and enclose variable and expressions inside {}
"""

# -------------------------------------------------------------------------------------------------------------------------

"""
there are various string methods that help in modifying the result
"""
print(string)
print(string.lower())
print(string.upper())
print(string.split(" "))
print(string.replace("a", "o"))

wide_space = "   Apple   "
print(wide_space)
print(wide_space.strip())

"""
Output:
Javascript Compendium
javascript compendium
JAVASCRIPT COMPENDIUM
['Javascript', 'Compendium']
Jovoscript Compendium
   Apple
Apple
"""

# -------------------------------------------------------------------------------------------------------------------------

"""
there are escape character that starts with \ and conducts modification to that string based on the character that appears after \ 
"""

print("Minecraft 'Mine \ craft'")
print("Mi\necraft 'Mi\ne \ craft'") # \n new line
print("Minecraf\t 'Mine \ craf\t'") # \t tab
print("Minecraft 'Mine \\ craft") # \\ cancel the escape character and makes it a single \
print(r"Mi\necraf\t 'Mine \craft'") # adding r infront makes it a raw string i.e. it appears without changes excluding escape character