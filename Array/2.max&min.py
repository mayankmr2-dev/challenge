array1 = [12, -1, 52, 22, 33, 10]
# set 1st element and second element set min and max and then compare using loop


def minandmax(array):
    min = array[0] if array[0] < array[1] else array[1]
    max = array[1] if array[1] > array[0] else array[0]
    for number in array[2:]:
        if number < min:
            min = number
        if number > max:
            max = number
    print(min, max)


if __name__ == "__main__":
    minandmax(array1)
