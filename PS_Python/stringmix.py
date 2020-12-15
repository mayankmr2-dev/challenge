# String problem
# Given two strings s1 and s2, create a mixed String
# contributed by ---> Dear friend Bengali

s1 = 'Abc'
s2 = 'Xyz'

final = ''


count = 0
while count < len(s2):
    for l in s1:
        final += (l+s2[::-1][count])
        count += 1
print(final)

'''
OUTPUT - 

AzbycX

'''
