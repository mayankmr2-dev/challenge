# Find duplicate item in array

# Time Complexity = O(n)

from collections import Counter

nums = [1, 3, 4, 2, 2]


def solution(N):
    freq = Counter(N)
    for item in freq:
        if freq[item] > 1:
            return item
        else:
            pass


def solution2(N):
    dic = {}
    for item in N:
        if item in dic:
            return item
        else:
            dic[item] = 1


def solution3(N):
    return max(N, key=N.count)


print(solution3(nums))
