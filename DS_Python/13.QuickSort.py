# Quick Sort
# Partition method - when a number is at the exact position
# Hoare Partitioning Scheme and Lomuto Partitioning Scheme

# Average Time Complexity - O(nlogn)
# Worst Time Complexity - O(n^2)
# Space Complexity - O(logn)
def swap(a, b, arr):
    arr[a], arr[b] = arr[b], arr[a]


def partition(elements, start, end):
    pivot_index = start
    pivot = elements[pivot_index]

    # to avoid cross
    while start < end:
        while start < len(elements) and elements[start] <= pivot:
            start += 1

        while elements[end] > pivot:
            end -= 1

        if start < end:
            swap(start, end, elements)

    swap(pivot_index, end, elements)
    return end


def quickSort(elements, start, end):
    if start < end:
        pi = partition(elements, start, end)
        quickSort(elements, start, pi-1)
        quickSort(elements, pi+1, end)


if __name__ == '__main__':
    elements = [11, 9, 29, 7, 2, 15, 28]
    elements1 = [1, 22, 3, 44, 5, 11]
    quickSort(elements, 0, len(elements)-1)
    print(elements)

    quickSort(elements1, 0, len(elements1)-1)
    print(elements1)
