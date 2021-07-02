# User function Template for python3

# array1 = [38, 9, 9, 29, 7, 2, 15, 28]
# 0.  1. 2.  3. 4. 5.  6.  7   length = 8

# Expected Time Complexity: O(N)
# Expected Auxiliary Space: O(1)

array1 = [38, 9, 9, 29, 7, 2, 15, 28]


def rotate(arr, n):
    x = arr[n - 1]  # 7  - 28

    for i in range(n - 1, 0, -1):
        arr[i] = arr[i - 1]

    arr[0] = x
    return arr


print(rotate(array1, len(array1)))
