# Bubble Sort
# Time complexity - O(n^2)
# Space complexity - O(1)


array1 = [38,9,29,7,2,15,28]

def bubblesort(arr):
    size = len(arr)
    for i in range(size-1):
        for j in range(size-1-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

print(bubblesort(array1))
