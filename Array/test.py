# Input:  arr[] = {1, 2, 3, 4, 5}
# Output: arr[] = {5, 1, 2, 3, 4}


ar1 = [-2, -3, 4, -1, -2, 1, 5, -3]


def solution(arr):
    n = len(arr)
    maxsize = 0
    maxrun = 0
    total = 0
    i = 0
    while i < n:
        total += arr[i]
        if total < 0:
            total = 0
        maxrun = max(total, arr[i])
        maxsize = max(maxsize, maxrun)
        i += 1
    return maxsize


print(solution(ar1))
