# Input: arr1[] = {1, 3, 4, 5, 7}
# arr2[] = {2, 3, 5, 6}
# Output: Union: {1, 2, 3, 4, 5, 6, 7}
# Intersection: {3, 5}


def Solution(a, b):
    intersection = set()
    for item in a:
        if item in b:
            intersection.add(item)
    return intersection


print(Solution([1, 3, 4, 5, 7], [2, 3, 5, 6]))

# Output - {3, 5}
