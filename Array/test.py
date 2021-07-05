
arr1 = [10, 0, 9, 8, 2, 7, 5]
arr2 = [5, 6, 7, 8, 9, 8, 7, 6, -1, 5, 6, 7, 8, 9, 0]

a1 = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
a2 = [0, 1, 2, 0, 1, 2]

ar1 = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
ar2 = [-1, -2, 0, 1, 3, -100, 2, 0, -4, 5]

arr4 = [1, 3, 3, 4, 5, 7]
arr5 = [5, -4, -2, 6, -1]
arr6 = [-2, -3, 4, -1, -2, 1, 5, -3]
arrt = [1, 2, 3, 0, 0, -100, -120, 4, 5]


def solution(arr):
    currentSum = 0
    maxSum = 0
    start_index = 0
    end_index = 0
    s = 0

    for i in range(len(arr)):
        currentSum += arr[i]
        if currentSum > maxSum:
            maxSum = currentSum
            start_index = s
            end_index = i
        elif currentSum < 0:
            currentSum = 0
            s += 1
        else:
            pass
    return maxSum, start_index, end_index


if __name__ == '__main__':
    print("this is a test")
    print(solution(arr6))
    # print(solution(arrt))
