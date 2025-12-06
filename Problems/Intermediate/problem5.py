"""
Sliding Window Max
Given a list and window size k, return list of maximums in each sliding window.

Example:
    max_window([1,3,-1,-3,5,3], 3) → [3,3,5,5]

Requirements:
-Solve without deque
-Must be O(n)-O(nk) depending on your logic (brute force allowed but optimized thinking is better)
"""

def max_window(lst, k):
    i = len(lst) + 1 - k
    result = []
    for x in range(i):
        m = max(lst[x:x+k])
        result.append(m)
    return result

print(max_window([1,3,-1,-3,5,3], 3))