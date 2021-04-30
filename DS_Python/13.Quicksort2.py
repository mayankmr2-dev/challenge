# Average Time Complexity - O(nlogn)
# Worst Time Complexity - O(n^2)
# Space Complexity - O(logn)
arr1 = [0, 9, 3, 8, 2, 7, 5]
arr2 = [5, 6, 7, 8, 9, 8, 7, 6, 5, 6, 7, 8, 9, 0]


def quicksort(arr):
    length = len(arr)
    if length <= 1:
        return arr

    pivot = arr.pop()

    items_greater = []
    items_smaller = []

    for item in arr:

        if item > pivot:
            items_greater.append(item)
        else:
            items_smaller.append(item)

    return quicksort(items_smaller) + [pivot] + quicksort(items_greater)


print(quicksort(arr1))
print(quicksort(arr2))
