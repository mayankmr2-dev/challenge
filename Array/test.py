# Input: -12, 11, -13, -5, 6, -7, 5, -3, -6
# Output: -12 -13 -5 -7 -3 -6 11 6 5


arr1 = [10, 0, 9, 8, 2, 7, 5]
arr2 = [5, 6, 7, 8, 9, 8, 7, 6, -1, 5, 6, 7, 8, 9, 0]

a1 = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
a2 = [0, 1, 2, 0, 1, 2]

ar1 = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
ar2 = [-1, -2, 0, 1, 3, -100, 2, 0, -4, 5]

arr4 = [1, 3, 3, 4, 5, 7]
# arr5 = [2, 3, 3, 5, 6]
arrt = [1, 2, 3, 4, 5]


def solution(arr):
    # put the last item in a variable
    final = len(arr)-1
    # run a for loop backwards from the second last item till the first
    for i in range(final-1, 0, -1):
        arr[i] = arr[i-1]
    # finally set the first item with the last item
    arr[0] = final
    return arr


if __name__ == '__main__':
    print("this is a test")
    print(solution(arrt))
    # print(solution(ar2))
