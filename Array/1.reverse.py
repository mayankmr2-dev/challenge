# Reverse an array


# 1. Slicing
list1 = [4, 5, 1, 2]
list2 = [18, 6, 2, 34, 12, 33, 20]
list3 = [12, 33, 4, 3, 4]
# print(list1[::-1])

# 2. reversed function
# print(list(reversed(list1)))
# for i in reversed(list1):
#     print(i)


# gfg
# def reverseList(A, start, end):
#     while start < end:
#         A[start], A[end] = A[end], A[start]
#         start += 1
#         end -= 1
#     return A

# def solution(arr):
#     length = len(arr)
#     for i in range(len(arr)//2):
#         arr[i], arr[length-1-i] = arr[length-1-i], arr[i]
#     return arr

# while i+=1  while i<len(arr)//2

# Time Complxity = O(n)

def reverseList(list1):
    i = 0
    while i < len(list1)//2:
        list1[i], list1[len(list1)-(i+1)] = list1[len(list1)-(i+1)], list1[i]
        i += 1
    return list1

# We did not go till the middle element bcoz it is not going to change hence i<xyz and not i<=xyz

#
# def solution(arr):
#     i = 0
#     j = len(arr)-1
#
#     while i < len(arr)//2:
#         arr[i], arr[j-i] = arr[j-i], arr[i]
#         i += 1
#     return arr


print(reverseList(list1))
print(reverseList(list2))
print(reverseList(list3))
