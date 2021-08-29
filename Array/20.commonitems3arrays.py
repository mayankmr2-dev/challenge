A = [1, 5, 10, 20, 40, 80]
B = [6, 7, 20, 80, 100]
C = [3, 4, 15, 20, 30, 70, 80, 120]
# Output: 20 80


def solution(arr1, arr2, arr3):
    n = len(arr1)
    m = len(arr2)
    l = len(arr3)

    i = 0
    j = 0
    k = 0

    result = []

    while i < n and j < m and k < l:

        if (arr1[i] == arr2[j] and arr2[j] == arr3[k]):
            result.append(arr1[i])

            i += 1
            j += 1
            k += 1

        elif arr1[i] < arr2[j]:
            i += 1

        elif arr2[j] < arr3[k]:
            j += 1

        else:
            k += 1

    return result


if __name__ == '__main__':
    print(solution(A, B, C))
    # [20, 80]
