
arr1 = [10, 0, 9, 8, 2, 7, 5]
arr2 = [5, 6, 7, 8, 9, 8, 7, 6, -1, 5, 6, 7, 8, 9, 0]

a1 = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
a2 = [0, 1, 2, 0, 1, 2]

ar1 = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
ar2 = [-1, -2, 0, 1, 3, -100, 2, 0, -4, 5]

arr4 = [1, 3, 3, 4, 5, 7]
arrt = [1, 2, 3, 0, 0, -100, -120, 4, 5]
arneg = [-1, -12, 0, -100]

# [0-low-1] [high+1-last]
ark1 = [1, 2, 4, 5, 6]
ark2 = [2, 3, 5, 7]

arr6 = [-2, -3, 4, -1, -2, 1, 5, -3]
arr7 = [1, -1, -2, -3, -4, -5]
arr5 = [5, -4, -2, 6, -1]
arneg = [-1, -12, 0, -100]

# lastindex = 7


def solution(arr):
    currentSum = 0
    maxSum = 0
    i = 0
    start_index = 0
    end_index = 0
    while i < len(arr):
        currentSum += arr[i]
        if currentSum <= 0:
            currentSum = 0
            i += 1

        else:
            if currentSum > maxSum:
                maxSum = currentSum
                start_index = i
                i += 1
            else:
                i += 1
    return maxSum


if __name__ == '__main__':
    print("this is a test")
    print(solution(arr6))
    print(solution(arr5))
    print(solution(arr7))
    print(solution(arneg))
