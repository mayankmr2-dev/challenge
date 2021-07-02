# Union and Intersection of two sorted arrays

# Input: arr1[] = {1, 3, 4, 5, 7}
# arr2[] = {2, 3, 5, 6}
# Output: Union: {1, 2, 3, 4, 5, 6, 7}
# Intersection: {3, 5}

# Optimal Solution
# Time Complexity = O(m+n)

arr1 = [1, 2, 4, 5, 6]
arr2 = [2, 3, 5, 7]


def printUnion(arr1, arr2, m, n):
    i, j = 0, 0
    final = []
    while i < m and j < n:
        if arr1[i] < arr2[j]:
            final.append(arr1[i])
            i += 1
        elif arr2[j] < arr1[i]:
            final.append(arr2[j])
            j += 1
        else:
            final.append(arr2[j])
            j += 1
            i += 1

    # Print remaining elements of the larger array
    while i < m:
        final.append(arr1[i])
        i += 1

    while j < n:
        final.append(arr2[j])
        j += 1

    return final


# Driver program to test above function
arr1 = [1, 2, 4, 5, 6]
arr2 = [2, 3, 5, 7]
m = len(arr1)
n = len(arr2)
print(printUnion(arr1, arr2, m, n))


# Time Complexity - O(m*n)
# Space Complexity - O(n)

arr1 = {1, 3, 4, 5, 7}
arr2 = {2, 3, 5, 6}


def solution(setarr1, setarr2):
    intersection = set()
    for item in setarr2:
        if item in setarr1:
            intersection.add(item)
        setarr1.add(item)

    return intersection, setarr1


# print(solution(arr1, arr2))
