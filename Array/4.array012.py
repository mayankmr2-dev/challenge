# Given an array of size N containing only 0s, 1s, and 2s
# sort the array in ascending order.
# DUTCH FLAG PROBLEM = O(n)
# space complexity = O(1)
# 0 0 0 1 1 1 2 2 2  -- keep the pointer at the middle ie. 1
# N = 5
# arr[]= {0 2 1 2 0}
# Output:
# 0 0 1 2 2


def sorting(arr):
    mid = 0
    low = 0
    high = len(arr)-1  # at the last no.
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr


if __name__ == "__main__":
    arr1 = [0, 1, 2, 0, 1, 2]
    arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
    print(sorting(arr1))
    print(sorting(arr))
