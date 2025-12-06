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