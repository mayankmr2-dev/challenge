# Prime Number

def primeNumber(a):
    if a < 2:
        return False
    else:
        for i in range(2, a):
            if a % 2 == 0:
                return False
        else:
            return True


print(primeNumber(23))
