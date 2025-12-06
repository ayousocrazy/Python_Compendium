"""
Balanced Bracket Checker
Write a function is_balanced(s) that checks if a string has balanced brackets:
    (), {}, []

Examples:
    "[({})]" → True  
    "[(])" → False  

Requirements:
-You must use a list as a stack.
-No using any library.
"""

def is_balanced(s):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for ch in s:
        if ch in "({[":
            stack.append(ch)
        else:
            if not stack:
                return False
            if stack.pop() != pairs[ch]: 
                return False

    return len(stack) == 0


# TESTS
print("Test 1:")
print(is_balanced("[{{{()}}}]"))