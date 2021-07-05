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
    for i in range(len(arr)):
        currentSum += arr[i]
        if currentSum > maxSum:
            maxSum = currentSum
        elif currentSum < 0:
            currentSum = 0
        else:
            pass
    return maxSum


print(solution(arr5))  # 6
print(solution(arr6))  # 7
print(solution(arr7))
