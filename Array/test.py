K = 6
arr1 = [1, 5, 7, 1]


def solution(arr, k):
    pairs = 0
    list_pairs = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i]+arr[j] == k:
                list_pairs.append((arr[i], arr[j]))
                pairs += 1
    return pairs, list_pairs


if __name__ == '__main__':

    print(solution(arr1, 6))
