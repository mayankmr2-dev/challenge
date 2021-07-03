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

arr4 = [1, 3, 3, 4, 5, 7]
arr5 = [2, 3, 3, 5, 6]


# Time Complexity = O(n+m)

def solution(ar1, ar2):
    low = 0
    med = 0
    final = []
    while low < len(ar1) and med < len(ar2):
        if ar1[low] < ar2[med]:
            low += 1
        elif ar2[med] < ar1[low]:
            med += 1
        else:  # in case both no.s are equal
            final.append(ar1[low])
            low += 1
            med += 1

    # This step is required when longer list is remaining and the other list is over
    while low < len(ar1):
        low += 1

    while med < len(ar2):
        med += 1

    return final


# Output - [3, 3, 5]
