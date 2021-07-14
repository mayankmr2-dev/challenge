arr1 = [1, 4, 3, 7, 1, 2, 6, 7, 6, 10]
arr2 = [2, 3, 1, 1, 4]
arr3 = [1, 1, 1, 1, 1]


def solution(arr, start, end):
    if (start == end):
        return 0

    if arr[start] == 0:
        return float('inf')

    minJumps = float('inf')

    for k in range(start+1, end+1):
        if (k <= start + arr[start]):
            jumps = solution(arr, k, end)

        if (jumps != minJumps and jumps+1 < minJumps):
            minJumps = jumps+1

    return minJumps


print(solution(arr2, 0, 4))
# print(solution(arr1, 0, 9))
# print(solution(arr3, 0, 4))
