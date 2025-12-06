"""
Matrix Rotator
Given a square matrix, rotate it 90° clockwise using only loops.

Example:
Input:
    1 2 3
    4 5 6
    7 8 9

Output:
    7 4 1
    8 5 2
    9 6 3
"""

def rotate(matrix):
    n = len(matrix)

    for row in matrix:
        if len(row) != n:
            return "Not a square matrix"
        
    result = [[0]*n for _ in range(n)]
    s = n - 1

    for ix in range(n):
        for iy in range(n):
            result[iy][s - ix] = matrix[ix][iy]

    return result

# TESTS
print("Test 1:")
m1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(f"Input:\n {m1}")
print(f"Output:\n{rotate(m1)}")

print("Test 2:")
m2 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]
print(f"Input:")
for x in m1:
    print(x)
print(f"Output:")
for x in rotate(m1):
    print(x)

print("Test 3:")
m3 = [
    [1, 2, 3],
    [4, 5, 6]
]
print(f"Input:")
for x in m3:
    print(x)
print(f"Output:")
print(rotate(m3))