import re

"""
regex (regular expression) is is used to search, match, extract, split, or replace patterns in text
"""

string = "You must be the change you want to see in the world"

m = re.search(r'world', string) # Searches the word 'world' in string
print(m)
print(m.start()) # starting index of 'world' in string
print(m.end()) # ending index of 'world' in string

"""
Output:
<re.Match object; span=(46, 51), match='world'>
46
51
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
