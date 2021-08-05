# Inversions in an array.

# Function to count Inversion Count


def mergeSort(arr, n):
    temp_arr = [0]*n
    return tmergeSort(arr, temp_arr, 0, n-1)

# This Function will use MergeSort to count inversions


def tmergeSort(arr, temp_arr, left, right):

    # Inversions_count
    inv_count = 0

    if left < right:

        # Mid of an array
        mid = (left + right)//2

        # calculating inversions_count for the left array.
        inv_count = tmergeSort(arr, temp_arr, left, mid)

        # calculating inversions_count for the right array.
        inv_count += tmergeSort(arr, temp_arr, mid + 1, right)

        # Merging two sorted arrays.
        inv_count += merge(arr, temp_arr, left, mid, right)
    return inv_count

# Merging two sorted arrays.


def merge(arr, temp_arr, left, mid, right):
    i = left
    j = mid + 1
    k = left
    inv_count = 0

    while i <= mid and j <= right:

        # No inversion if arr[i] <= arr[j]

        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            k += 1
            i += 1
        else:
            # Inversion will occur if arr[i] > arr[j]
            temp_arr[k] = arr[j]
            inv_count += (mid-i + 1)
            k += 1
            j += 1

    # The remaining elements of leftarray are copied
    while i <= mid:
        temp_arr[k] = arr[i]
        k += 1
        i += 1

    # The remaining elements of right array are copied
    while j <= right:
        temp_arr[k] = arr[j]
        k += 1
        j += 1

    for loop_var in range(left, right + 1):
        arr[loop_var] = temp_arr[loop_var]

    return inv_count


# Driver
# Given array is
arr = [83, 20, 9, 50, 115, 61, 17]
# 1st no. greater than following no. like 83 > 20
# arr = [83, 20, 9, 50, 115]
n = len(arr)
result = mergeSort(arr, n)
print("Inversions_count =", result)  # 11
