ar1 = [7, 1, 5, 3, 6, 4]


def solution(arr):
    n = len(arr)
    left = 0
    right = 1
    maxP = 0

    while right < n:
        if(arr[right] <= arr[left]):
            left = right
        else:
            diff = arr[right] - arr[left]
            maxP = max(maxP, diff)
        right += 1
    return maxP


if __name__ == '__main__':
    print(solution(ar1))
