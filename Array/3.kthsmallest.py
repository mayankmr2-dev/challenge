# Given an array arr[] and a number K where K
# is smaller than size of array, the task is to
# find the Kth smallest element in the given array.
# It is given that all array elements are distinct.

# N = 6
# arr[] = 7 10 4 3 20 15
# K = 3
# Output = 7

# Try to use QuickSelect - Quicksort variant


def kthsmallest(arr, n):
    final = sorted(arr, reverse=True)
    return final[-n]


if __name__ == "__main__":
    arr1 = [7, 10, 4, 3, 20, 15]
    print(kthsmallest(arr1, 3))
