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


def reverseList(list1):
    i = 0
    while i < len(list1)//2:
        list1[i], list1[len(list1)-(i+1)] = list1[len(list1)-(i+1)], list1[i]
        i += 1
    return list1


print(reverseList(list1))
print(reverseList(list2))
print(reverseList(list3))
