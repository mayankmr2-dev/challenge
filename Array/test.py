K = 6
arr1 = [1, 5, 7, 1]


def solution(arr, k):
    n = len(arr)
    pairs = 0
    left = 0
    right = 1
    sum = 0
    while right < n:
        sum += (arr[left] + arr[right])
        if sum == k:
            pairs += 1
            sum -= arr[left]
            left = right
        right += 1
    return pairs


if __name__ == '__main__':

    print(solution(arr1, 6))
