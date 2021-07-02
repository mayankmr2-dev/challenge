# Move all negative numbers to beginning
# Input: -12, 11, -13, -5, 6, -7, 5, -3, -6
# Output: -12 -13 -5 -7 -3 -6 11 6 5

# Time Complexity - O(n)
# Space Complexity - O(n)

array1 = [-12, 11, -13, -5, 6, -7, 5, -3, -6]


def solution(arr):
    if len(arr) <= 1:
        return arr

    pivot = 0

    negative = []
    positive = []

    for item in arr:

        if item > pivot:
            positive.append(item)
        else:
            negative.append(item)

    negative.extend(positive)
    return negative

# Optimized solution

# Time Complexity - O(n)
# Space Complexity - O(1)


def solution2(arr):
    j = 0
    for i in range(len(arr)):
        if arr[i] < 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
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
    print(solution(array1))
