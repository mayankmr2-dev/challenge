
def findSquare(num):

    # convert number to positive if it is negative
    num = abs(num)

    # stores square of the number
    sq = num

    # repeatedly add num to the result
    for i in range(1, num):
        sq = sq + num

    return sq


if __name__ == '__main__':

    print(findSquare(8))
    print(findSquare(-4))
