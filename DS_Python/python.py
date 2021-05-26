# Bubble Sort

array1 = [12, 3, 4, 9, 5, 1, 9]


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    middle = len(arr)//2

    left, right = merge_sort(arr[:middle]), merge_sort(arr[middle:])

    return merge(left, right)


def merge(left, right):
    result = []
    left_pointer = right_pointer = 0

    while left_pointer < len(left) and right_pointer < len(right):

        if left[left_pointer] < right[right_pointer]:
            result.append(left[left_pointer])
            right_pointer += 1
