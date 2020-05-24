# Fibonacci Numbers

# 0 1 1 2 3 5 8 .....


def fib(n):
    a = 0
    b = 1

    if n == 1:
        print(a)
    else:
        print(a, end=' ')
        print(b, end=' ')
        for i in range(2, n):
            c = a+b
            a = b
            b = c
            print(c, end=' ')


# fib(6)  # Output - 0 1 1 2 3 5

# Using generator function
def fibb(n):
    a = 0
    b = 1
    for j in range(n):
        yield a
        a, b = b, a+b


result = fibb(6)
print(list(result))  # Output - [0, 1, 1, 2, 3, 5]
