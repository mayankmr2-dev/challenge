# Insertion sort
# Worst Case Time Complexity[Big-O]: O(n2)

# Best Case Time Complexity[Big-omega]: O(n)

# Average Time Complexity[Big-theta]: O(n2)

# Space Complexity: O(1)

def insertion_sort(list_a):
    indexing_length = range(1, len(list_a))
    for i in indexing_length:
        value_to_sort = list_a[i]

        while list_a[i-1] > value_to_sort and i > 0:
            list_a[i-1], list_a[i] = list_a[i], list_a[i-1]
            i -= 1

    return list_a


print(insertion_sort([3, 2, 5, 7, 4]))
