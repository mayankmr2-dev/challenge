
# Bubble sort

arr1 = [10, 0, 9, 8, 2, 7, 5]
arr2 = [5, 6, 7, 8, 9, 8, 7, 6, -1, 5, 6, 7, 8, 9, 0]

# Input: {0, 1, 2, 0, 1, 2}
# Output: {0, 0, 1, 1, 2, 2}
#
# Input: {0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1}
# Output: {0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2}

a1 = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
a2 = [0, 1, 2, 0, 1, 2]


# def solution(arr):
#     set1 = set()
#     for item in arr:
#         set1.add(item)
#     return set1

def solution(arr):
    length = len(arr)
    for i in range(len(arr)//2):
        arr[i], arr[length-1-i] = arr[length-1-i], arr[i]
    return arr


if __name__ == '__main__':
    print("this is a test")
    print(solution(arr1))
    print(solution(arr2))
