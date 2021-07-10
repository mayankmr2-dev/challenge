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


# Intersection of arrays

# Time Complexity - O(m+n)
# Space Complexity - O(n)

arr1 = {1, 3, 4, 5, 7}
arr2 = {2, 3, 5, 6}


def solution(ar1, ar2):
    new = []
    for item in ar1:
        if item in ar2:
            new.append(item)
        else:
            pass
    return new
# print(solution(arr1, arr2))


def solutionkk(arr1, arr2):
    upperptr = 0
    lowerptr = 0
    result = []
    while upperptr < len(arr1) and lowerptr < len(arr2):
        if arr1[upperptr] < arr2[lowerptr]:
            # result.append(arr1[upperptr])
            upperptr += 1
        elif arr2[lowerptr] < arr1[upperptr]:
            # result.append(arr2[lowerptr])
            lowerptr += 1
        elif arr2[lowerptr] == arr1[upperptr]:
            result.append(arr2[lowerptr])
            lowerptr += 1
            upperptr += 1
    while upperptr < len(arr1):
        # result.append(arr1[upperptr])
        upperptr += 1
    while lowerptr < len(arr2):
        # result.append(arr2[lowerptr])
        lowerptr += 1
    return len(result), result
