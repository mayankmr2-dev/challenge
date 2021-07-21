# Merge two sorted arrays without using extra space O(1)
# Time complexity - O(nm) worse case  O(nmlogm)

arr1 = [1, 3, 5, 7]
n = 4
arr2 = [0, 2, 6, 8, 9]
m = 5


def solution(arr1, n, arr2, m):
    i = n - 1
    while i >= 0:
        j = 0
        while j < m:
            if arr1[i] > arr2[j]:
                arr1[i], arr2[j] = arr2[j], arr1[i]
                i -= 1
                j += 1
            else:
                i -= 1
                j += 1
    arr1.sort()
    arr2.sort()
    return arr1, arr2


print(solution(arr1, n, arr2, m))
