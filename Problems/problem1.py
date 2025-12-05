"""
Frequency Compressor
Write a function compress(arr) that takes a list and returns a run-length encoded version

Example:
compress([1,1,1,2,2,3,1]) → [(1,4), (2,2), (3,1)]

Requirements:
-Must use loops only (no built-ins like itertools.groupby).
-Must return a list of tuples.
-Handle empty lists and lists with mixed data types
"""

def compress(arr):
    if arr == []:
        return []

    count = []

    for x in arr:
        found = False

        for idx, (value, c) in enumerate(count):
            if x == value:
                count[idx] = (value, c + 1)
                found = True
                break

        if not found:
            count.append((x, 1))

    return count


print(compress([1,1,1,2,2,3,1]))