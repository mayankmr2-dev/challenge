# Minimize the number of jumps to reach till the end

# Greedy algorithm
ar = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
ar1 = [1, 1, 1, 1, 1]


#  if len == 1 return 0
#  if arr[0] == 0 return -1
def solution(arr):
    maxR = arr[0]
    steps = arr[0]
    jumps = 1

    for i in range(1, len(arr)):
        if (i == len(arr)-1):
            return jumps

        maxR = max(maxR, i + arr[i])
        steps -= 1

        if (steps == 0):
            jumps += 1
            if (i >= maxR):
                return -1
            else:
                steps = maxR - i


print(solution(ar))
print(solution(ar1))


# Recursion

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

# Dynamic Programming


ar1 = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]


def minJumpsDP(arr):
    # if the start index is 0 we can't go anywhere
    if arr[0] == 0:
        return float('inf')

    endIndex = len(arr)

    # init OPT array
    OPT = [0 for i in range(endIndex)]

    for i in range(1, endIndex):
        OPT[i] = float('inf')  # 999999
        for j in range(0, i):
            # if i is reachable from j
            if i <= j + arr[j]:   # j + arr[j] shows max reach
                OPT[i] = min(OPT[i], OPT[j] + 1)
    return OPT[-1]


print(minJumpsDP(ar1))
