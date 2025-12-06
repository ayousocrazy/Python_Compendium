"""
Custom Sorting
Implement your own sorting function my_sort(arr, reverse=False).

Requirements:
-Pure loops.
-No sort() or sorted().
-Must accept a reverse=True flag
"""

def my_sort(arr, reverse=False):
    if not arr:
        return arr

    first_type = type(arr[0])

    if first_type in (int, float):
        allowed = (int, float)
    elif first_type is str:
        allowed = (str,)
    else:
        raise TypeError("Unsupported type")

    for x in arr:
        if not isinstance(x, allowed):
            raise TypeError("Type mismatch in array elements")

    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):

            if reverse:
                if arr[i] < arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
            else:
                if arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]

    return arr

# TESTS
print("Test 1:")
print(my_sort([11, 33, 22, 66, 44, 55, 111, 99]))

print("Test 2:")
print(my_sort([11, 33, 22, 66, 44, 55, 111, 99], True))

print("Test 3:")
print(my_sort(["Earth", "Venus", "Mars", "Mercury", "Saturn", "Jupiter", "Uranus", "Neptune"]))