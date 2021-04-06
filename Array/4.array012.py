# Given an array of size N containing only 0s, 1s, and 2s
# sort the array in ascending order.
# DUTCH FLAG PROBLEM = O(n)
# 0 0 0 1 1 1 2 2 2  -- keep the pointer at the middle ie. 1
# N = 5
# arr[]= {0 2 1 2 0}
# Output:
# 0 0 1 2 2


def sorting(arr):
    m = l = 0
    n = len(arr)
    h = n - 1
    while m <= h:
        if arr[m] == 0:
            arr[l], arr[m] = arr[m], arr[l]
            m += 1
            l += 1
        elif arr[m] == 1:
            m += 1
        else:
            arr[m], arr[h] = arr[h], arr[m]
            h -= 1
    return arr


if __name__ == "__main__":
    arr1 = [0, 1, 2, 0, 1, 2]
    arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
    print(sorting(arr1))
    print(sorting(arr))
