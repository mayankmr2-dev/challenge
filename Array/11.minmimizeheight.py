# Minimize the maximum difference between heights
# Array has to be sorted before any operation
ar = [1, 10, 14, 14, 14, 15]
k = 6


ar2 = [3, 9, 16, 12, 20]

ar3 = [1, 10, 14, 14, 14, 15]


def solution(arr, k):
    ans = arr[len(arr)-1]-arr[0]
    smallest = arr[0] + k
    largest = arr[len(arr)-1] - k
    # minimum = 0
    # maximum = 0

    for i in range(len(arr)-1):
        p = arr[i+1]-k
        q = arr[i]+k
        minimum = min(smallest, p)
        maximum = max(largest, q)

        if (minimum < 0):
            continue

        ans = min(ans, maximum - minimum)

    return ans


print(solution(ar, k))  # 5
print(solution(ar2, 3))  # 11
print(solution(ar3, 6))  # 5
