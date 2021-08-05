# Next Permutation - check from last, 7 should be greater than 4 arr[i] > arr[i-1]
# Time Complexity - O(n) worst O(n!)
# Space Complexity - O(1a)


list1 = [1, 5, 8, 4, 7, 6, 5, 3, 1]
list2 = [5, 4, 3, 2, 1]
list3 = [1, 2, 3]
list4 = [0, 1]
list5 = [1]


def solution(arr):
    idx = -1
    n = len(arr)
    for i in range(n-1, -1, -1):
        if arr[i] > arr[i-1]:
            idx = i
            break

    if (idx == -1):
        arr.reverse()
    else:
        prev = idx
        for i in range(idx+1, n):
            if arr[i] > arr[idx-1] and arr[i] <= arr[prev]:
                prev = i

        arr[idx-1], arr[prev] = arr[prev], arr[idx-1]
        arr[idx:] = sorted(arr[idx:])

    return arr


print(solution(list1))  # [1, 5, 8, 5, 1, 3, 4, 6, 7]
print(solution(list2))  # [1, 2, 3, 4, 5]
print(solution(list3))  # [1, 3, 2]
print(solution(list4))  # [1, 0]
print(solution(list5))  # [1]
