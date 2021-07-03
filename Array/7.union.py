# Complete doUnion funciton that takes a, n, b, m as parameters
# and returns the count of union elements of the two arrays.
# The printing is done by the driver code.

# Constraints:
# 1 ≤ n, m ≤ 105
# 1 ≤ a[i], b[i] < 105

# Expected Time Complexity: O((n+m)log(n+m))
# Expected Auxilliary Space: O(n+m)

# Input:
# 5 3
# 1 2 3 4 5
# 1 2 3

# Output:
# 5

# Explanation:
# 1, 2, 3, 4 and 5 are the
# elements which comes in the union set
# of both arrays. So count is 5.
# a [] n elements , b [] m elements

# Constraints:
# 1 ≤ n, m ≤ 105
# 1 ≤ a[i], b[i] < 105

# Expected Time Complexity: O((n+m)log(n+m))
# Expected Auxilliary Space: O(n+m)

class Solution:
    # Function to return the count of number of elements in union of two arrays.
    def doUnion(self, a, n, b, m):
        final = set()

        for i in range(n):
            final.add(a[i])

        for j in range(m):
            final.add(b[j])

        return len(final)


# Time Complexity = O(n+m)

def solution(ar1, ar2):
    low = 0
    med = 0
    final = []
    while low < len(ar1) and med < len(ar2):
        if ar1[low] < ar2[med]:
            final.append(ar1[low])
            low += 1
        elif ar2[med] < ar1[low]:
            final.append(ar2[med])
            med += 1
        else:  # in case both no.s are equal
            final.append(ar1[low])
            low += 1
            med += 1

    # This step is required when longer list is remaining and the other list is over
    while low < len(ar1):
        final.append(ar1[low])
        low += 1

    while med < len(ar2):
        final.append(ar2[med])
        med += 1

    return final


# def solution(ar1, ar2):
#     for item in ar2:    O(n+m)
#         if item not in ar1:
#             ar1.append(item)
#         else:
#             pass
#     ar1.sort()   O(nlogn)
#     return ar1
if __name__ == "__main__":
    obj = Solution()
    print(obj.doUnion([1, 2, 3, 4, 5], 5, [1, 2, 3], 3))  # result = 5
    print(obj.doUnion([1, 1, 2, 2, 3, 3], 6, [8, 9, 7, 6, 5], 5))  # result = 8
