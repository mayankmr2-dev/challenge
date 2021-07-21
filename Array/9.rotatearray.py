# User function Template for python3

# array1 = [38, 9, 9, 29, 7, 2, 15, 28]
# 0.  1. 2.  3. 4. 5.  6.  7   length = 8

# Expected Time Complexity: O(N)
# Expected Auxiliary Space: O(1)

array1 = [38, 9, 9, 29, 7, 2, 15, 28]


def solution(arr):
    n = len(arr)
    x = arr[n - 1]
     
    for i in range(n - 1, 0, -1):
        arr[i] = arr[i - 1];
         
    arr[0] = x;
    return arr



# def solution(arr):
#     n = len(arr)
#     lastitem = arr[-1]

#     for i in range(n-2, -1, -1):
#         arr[i+1] = arr[i]

#     arr[0] = lastitem
#     return arr



# Time complexity = O(n)

# def solution(arr):
#     last = arr.pop()
#     arr.insert(0, last)
#     return arr


print(rotate(array1, len(array1)))
