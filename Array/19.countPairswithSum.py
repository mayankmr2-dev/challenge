# Count Pairs with given sum
# Time Complexity - O(N)
# Space complexity - O(N)

ar1 = [2, 6, 9, 3, 4, 5, 2]
# k = 8


def solution(arr, k):
    n = len(arr)
    counter = 0
    map_no = {}

    for i in range(n):

        if (arr[i] < k):
            element = k - arr[i]

            if (element in map_no):
                counter += map_no[element]

            if (arr[i] not in map_no):
                map_no[arr[i]] = 0

            value = map_no.get(arr[i])
            map_no[arr[i]] = value + 1
        else:
            continue

    return counter


print(solution(ar1, 8))
# output - 3
