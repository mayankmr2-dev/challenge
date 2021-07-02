# Bubble Sort

array1 = [12, 3, 4, 9, 5, 1, 9]


def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    midpoint = len(arr)//2
    left, right = mergeSort(arr[:midpoint]), mergeSort(arr[midpoint:])

    return merge(left, right)


def merge(left, right):
    result = []
    left_pointer = right_pointer = 0

    while left_pointer < len(left) and right_pointer < len(right):

        if left[left_pointer] < right[right_pointer]:
            result.append(left[left_pointer])
            left_pointer += 1
        else:
            result.append(right[right_pointer])
            right_pointer += 1

    result.extend(left[left_pointer:])
    result.extend(right[right_pointer:])

    return result


if __name__ == '__main__':
    print(mergeSort(array1))
