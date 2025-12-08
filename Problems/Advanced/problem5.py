"""
Generate All Balanced Parentheses
Problem Statement
Given n pairs of parentheses, write a recursive function to generate all possible balanced parentheses strings of length 2n.

Example
Input: n = 3
Output (order doesn't matter):
    "((()))"
    "(()())"
    "(())()"
    "()(())"
    "()()()"

Rules / Constraints
-A string is balanced if each opening ( has a corresponding closing ) and parentheses are properly nested.
-You cannot use loops—only recursion.
-You can pass extra arguments in the recursion (like current string, counts of open and close parentheses).
"""

def generate_parentheses(n):
    result = []

    def backtrack(current, open_count, close_count):
        if len(current) == 2 * n:
            result.append(current)
            return

        if open_count < n:
            backtrack(current + "(", open_count + 1, close_count)

        if close_count < open_count:
            backtrack(current + ")", open_count, close_count + 1)

    backtrack("", 0, 0)
    return result


# TEST
for p in generate_parentheses(4):
    print(p)