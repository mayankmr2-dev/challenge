# Move all negative numbers to beginning
# Input: -12, 11, -13, -5, 6, -7, 5, -3, -6
# Output: -12 -13 -5 -7 -3 -6 11 6 5

# Time Complexity - O(2n)
# Space Complexity - O(n)

array1 = [-12, 11, -13, -5, 6, -7, 5, -3, -6]


def solution(arr):
    if len(arr) <= 1:
        return arr
    neg = []
    pos = []
    for item in arr:
        if item < 0:
            neg.append(item)
        else:
            pos.append(item)
    neg.extend(pos)
    return neg

# Optimized solution

# Time Complexity - O(n)
# Space Complexity - O(1)

# low mid first half of dutch flag


def solution2(arr):
    low = 0
    mid = 0

    # while mid < len(arr)
    for mid in range(len(arr)):
        if arr[mid] < 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        else:
            mid += 1
    return arr


# Two pointer approach
# left, right
# take neg and 0s as one

# mid high second half of dutch flag

def solution(arr):
    left = 0
    right = len(arr)-1
    while left <= right:
        if arr[left] < 0:
            left += 1
        else:
            arr[left], arr[right] = arr[right], arr[left]
            right -= 1
    return arr

# Worst case - using quicksort
# Time Complexity - O(nlogn)
# Space Complexity - O(n)


def solution3(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr.pop()
    neg = []
    pos = []

    for item in arr:
        if item < pivot:
            neg.append(item)
        else:
            pos.append(item)

    return solution3(neg) + [pivot] + solution3(pos)


if __name__ == "__main__":
    print(solution3(array1))
