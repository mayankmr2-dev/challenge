# Sum of largest contigous subarray within an array
# Kadane's Algorithm

arr5 = [5, -4, -2, 6, -1]
arr6 = [-2, -3, 4, -1, -2, 1, 5, -3]
arr7 = [1, -1, -2, -3, -4, -5]
# in case all no. are negative then just find the no. which is smallest
# Time Complexity - O(n)


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
    return maxSum, start_index, end_index


arneg = [-1, -12, 0, -100]


def solution1(arr):
    currentSum = 0
    maxSum = 0
    for i in arr:
        currentSum += i
        currentSum = max(i, currentSum)
        maxSum = max(currentSum, maxSum)
    return maxSum


def solutionkk(arr):
    currentSum = 0
    maxSum = 0
    i = 0
    start_index = 0
    end_index = 0
    s = 0
    while i < len(arr):
        currentSum += arr[i]
        if currentSum <= 0:
            currentSum = 0
            i += 1
            s += 1

        else:
            if currentSum > maxSum:
                maxSum = currentSum
                start_index = s
                end_index = i
                i += 1
            else:
                i += 1
    return maxSum, (start_index, end_index)

# def solution(arr):
#     n = len(arr)
#     maxsize = 0
#     maxrun = 0
#     total = 0
#     i = 0
#     while i < n:
#         total += arr[i]
#         if total < 0:
#             total = 0
#         maxrun = max(total, arr[i])
#         maxsize = max(maxsize, maxrun)
#         i += 1
#     return maxsize


print(solution(arr5))  # 6 (6, 1, 3)
print(solution(arr6))  # 7 (7, 2, 6)
print(solution1(arr7))  # 1
print(solution1(arneg))  # 0
