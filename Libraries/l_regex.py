import re

"""
regex (regular expression) is is used to search, match, extract, split, or replace patterns in text
"""

string = "You must be the change you want to see in the world"

m = re.search(r'world', string) # Searches the word 'world' in string
print(m)
print(m.start()) # starting index of 'world' in string
print(m.end()) # ending index of 'world' in string
print(m.group(0))

"""
Output:
<re.Match object; span=(46, 51), match='world'>
46
51
world
"""

# -------------------------------------------------------------------------------------------------------------------------

text = '12345 is not a plaindrome number, neither is 54321. But 123454321 is plaindrome'

search1 = r"\d+" # \d+ takes one or more numbers
search2 = r"\d" # \d takes one digit
search3 = r"\d*" # \d* takes zero or more digits i.e "" and number
search4 = r"\d{5}" #\d{num} takes num digits
search5 = r"\d{5,10}" # \d{num1,num2} tales num1 to num2 digits

search6 = r"\D+" # \D takes non digit
search7 = r"\w+" # \w takes word character (0-9), (a-z), (A-Z), (_)
search8 = r"\W+" # \W takes non word character ( )space, (@, -) 
search9 = r"\s+" # \s takes whitespace (space, tab, newline)
search10 = r"\S+" # \S takes non whitespace (letter and numbers)

search11 = r"^" # ^ takes start of string
search12 = r"$" # $ takes end of string
search13 = r"\bplaindrome\b" # \bpattern\b takes whole word, not as part of another word
search14 = r"\Bdrom\B" # \Bpattern\B only when pattern is inside a word

# \D, \w, \W, \s, \S also works with quantifier +, *, {} as in \d

print(re.findall(search1, text)) # finds all the non-overlapping pattern and returns as list
print(re.findall(search2, text))
print(re.findall(search3, text))
print(re.findall(search4, text))
print(re.findall(search5, text))
print(re.findall(search6, text))
print(re.findall(search7, text))
print(re.findall(search8, text))
print(re.findall(search9, text))
print(re.findall(search10, text))
print(re.findall(search11, text))
print(re.findall(search12, text))
print(re.findall(search13, text))
print(re.findall(search14, text))

"""
Output:
['12345', '54321', '123454321']
['1', '2', '3', '4', '5', '5', '4', '3', '2', '1', '1', '2', '3', '4', '5', '4', '3', '2', '1']
['12345', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '54321', '', '', '', '', '', '', '123454321', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
['12345', '54321', '12345']
['12345', '54321', '123454321']
[' is not a plaindrome number, neither is ', '. But ', ' is plaindrome']
['12345', 'is', 'not', 'a', 'plaindrome', 'number', 'neither', 'is', '54321', 'But', '123454321', 'is', 'plaindrome']
[' ', ' ', ' ', ' ', ' ', ', ', ' ', ' ', '. ', ' ', ' ', ' ']
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
['12345', 'is', 'not', 'a', 'plaindrome', 'number,', 'neither', 'is', '54321.', 'But', '123454321', 'is', 'plaindrome']
['']
['']
['plaindrome', 'plaindrome']
['drom', 'drom']

these symbols like \d, \d+ are called character class and metaclasses
"""

# -------------------------------------------------------------------------------------------------------------------------

string = 'Because that is the only way he can pay me. He has no money. Are we poor, Atticus?'
pattern = re.compile('[a-e]') # compiles an regex to pattern object
# it creates a pattern a, b, c, d, e does not include uppercase

print(pattern)
print(pattern.findall(string)) # returns each occurrence of pattern in the string

pattern = re.compile('\w+') # converts a regex pattern string to a regex object so that we don't have to write it everytime
print(pattern.findall(string))

pattern = re.compile('[a-e]', re.IGNORECASE) # Create object with re flag IGNORECASE
print(pattern.findall(string))

pattern = re.compile('ab*') # returns occurrence of ab followed by 0 or more b
print(pattern.findall("ababbaabbb"))

"""
Output:
re.compile('[a-e]')
['e', 'c', 'a', 'e', 'a', 'e', 'a', 'e', 'c', 'a', 'a', 'e', 'e', 'a', 'e', 'e', 'e', 'c']
['Because', 'that', 'is', 'the', 'only', 'way', 'he', 'can', 'pay', 'me', 'He', 'has', 'no', 'money', 'Are', 'we', 'poor', 'Atticus']
['B', 'e', 'c', 'a', 'e', 'a', 'e', 'a', 'e', 'c', 'a', 'a', 'e', 'e', 'a', 'e', 'A', 'e', 'e', 'A', 'c']
['ab', 'abb', 'a', 'abbb'] # a is valid cause a is accompanied by 0*b
"""

# -------------------------------------------------------------------------------------------------------------------------

print(re.split(r'\d+', "Do things you like only 2 times, (day and night); or 4 times(morning, afternoon, evening and night)"))
# splits string based on numbers

print(re.split('[a-e]', "drop the beat", flags=re.IGNORECASE))
# splits string based in a-e ignoring the case 

pattern = re.compile(r'\W+')

print(re.split(pattern, "An apple a day empties the apple basket", maxsplit=4))
# splits string based on non-word character and maxsplit sets limit to number of splits by 4 i.e there will be max 5 items in list

# .split() splits the string to list as per given pattern

"""
output:
['Do things you like only ', ' times, (day and night); or ', ' times(morning, afternoon, evening and night)']
['', 'rop th', ' ', '', '', 't']
['An', 'apple', 'a', 'day', 'empties the apple basket']
"""

# -------------------------------------------------------------------------------------------------------------------------

print(re.sub('and', '&','bread and butter, peanut And butter'))
# re.sub replaces a pattern with replacement string 

print(re.sub('and', '&','bread and butter, peanut And butter', flags=re.IGNORECASE))
# can add flags=re.IGNORECASE to replace irrespective to case

pattern = re.compile(r'\d+')
replacement = "number"
print(re.sub(pattern, replacement, "6 7 has been cringe", count=1))
# adding count only changes the count number of pattern 

"""
Output:
bread & butter, peanut And butter
bread & butter, peanut & butter
number 7 has been cringe
"""

# -------------------------------------------------------------------------------------------------------------------------

string = "not being common and not being different is not being anything"

replaced = re.subn(r"\sNOT\s", "!", string, flags=re.IGNORECASE)

print(replaced)
# .subn is same as sub but it also returns the number of occurrence replaced as well as a tuple
print(replaced[0])
print(replaced[1])

"""
Output:
('not being common and!being different is!being anything', 2)
not being common and!being different is!being anything
2
"""

# -------------------------------------------------------------------------------------------------------------------------

print(re.escape("[Killing a mocking bird] is the first book I read"))
# .escape adds a backslash (\) before all special characters in a string

"""
Output:
\[Killing\ a\ mocking\ bird\]\ is\ the\ first\ book\ I\ read
"""

# -------------------------------------------------------------------------------------------------------------------------

"""
Meta-characters
"""

match = re.findall(r"[a-l]", "All that glitters is not gold — sometimes it’s just cheap glitter", flags=re.IGNORECASE)
# [] brackets represent character class here [a-l] represent [abcdefghijkl]
print(match)

match = re.findall(r"[^a-l]", "All that glitters is not gold — sometimes it’s just cheap glitter", flags=re.IGNORECASE)
# ^ inside [] represents character except a-l. [^a-l] represents [mnopqrstuvwxyz1234567890] also special characters and space
print(match)

for x in ["Safe is better than sorry", "Better late than never — but never is often on time.", "Better known than liked — welcome to the internet."]:
    if re.search(r"^better", x, flags=re.IGNORECASE):
        # ^ checks if string starts with the pattern 
        print(x)

for x in ["Safe is better than sorry.", "Better late than never — but never is often on time.", "Better known than liked — welcome to the internet"]:
    if re.search(r"\.$", x, flags=re.IGNORECASE):
        # $ checks if string ends with the pattern 
        print(x)

for x in ["apple", "apex", "ape", "pie", "apppppp", "aep"]:
    if (match:= re.search(r"a.p", x)):
        # a.p matches any three consecutive characters: 'a', followed by any single character, followed by 'p'
        print(x)

print(re.findall(r".", "A.P.T"))
# Here I want to find all .'s but it is using the meta character . 

print(re.findall(r"\.", "A.P.T"))
# adding \ infront of meta character makes it a common character

pattern = re.compile(r'a..d|x$')
# | acts as a or operator checking either of the patterns
for x in ["abcd", "abcx", "bcd", "acd", "cd", "cdzx"]:
    if pattern.search(x):
        print(x)

print("\n")
for x in ["aaad", "abcx", "bcad", "acd", "ad", "cdzx"]:
    if match:= re.search(r'a*d', x):
        # * represents 0 or more occurence of a followed by d
        # 0 or more occurence applies to character immediate before of * sign 
        print(x)

print("\n")
for x in ["aaad", "abcx", "bcad", "acd", "ad", "cdzx"]:
    if match:= re.search(r'a+d', x):
        # + represents 1 or more occurence of a followed by d
        # 1 or more occurence applies to character immediate before of + sign 
        print(x)

print("\n")
for x in ["aab", "ape", "aaabra", "dbra"]:
    if re.search(r'a{2,4}', x):
        # {2, 4} prints when a continiously occurs 2-4 times
        print(x)

for x in ["aba", "apex", "ape", "xbram", "aaba"]:
    if re.search(r"(^a|^x)b|x$", x):
        # () sign helps to group pattern 
        print(x)

print('\n')
for x in ["abc", "abb", "abbc", "acd", "dabc"]:
    if re.search(r"ab?c", x):
        # ? indicates that the character immediate before ? can occur none or once
        print(x)

# -------------------------------------------------------------------------------------------------------------------------