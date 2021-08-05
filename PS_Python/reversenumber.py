
def ulta(number):
    revs_number = 0

    # reverse the integer number using the while loop

    while (number > 0):
        # Logic
        remainder = number % 10
        revs_number = (revs_number * 10) + remainder
        number = number // 10

    return revs_number


print(ulta(1234))
