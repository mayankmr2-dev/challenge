# User function Template for python3

# array1 = [38, 9, 9, 29, 7, 2, 15, 28]
# 0.  1. 2.  3. 4. 5.  6.  7   length = 8

# Expected Time Complexity: O(N)
# Expected Auxiliary Space: O(1)

array1 = [38, 9, 9, 29, 7, 2, 15, 28]


def rotate(arr, n):
    # put the last item in a variable
    final = len(arr)-1

    # run a for loop backwards from the second last item till the first
    for i in range(final-1, 0, -1):
        arr[i] = arr[i-1]

    # finally set the first item with the last item
    arr[0] = final
    return arr


# Time complexity = O(n)

# def solution(arr):
#     last = arr.pop()
#     arr.insert(0, last)
#     return arr


print(rotate(array1, len(array1)))
