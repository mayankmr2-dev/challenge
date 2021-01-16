# Hash Map with collision
# Suppose you want to feed multiple data in the same index of the array
# As it get overwritten , we have to add it as a list in the respective index


class HashMap:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        total = 0
        for i in key:
            num = ord(i)
            total += num
        final = total % self.MAX
        return final

    def __setitem__(self, key, value):
        h = self.get_hash(key)  # gives number - eg. 8
        Found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, value)
                Found = True
                break
        if not Found:
            self.arr[h].append((key, value))

    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                print(element[1])
                break
        else:
            print("NOT FOUND !")

    def __delitem__(self, key):
        h = self.get_hash(key)
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h].pop(idx)
                break

    def __str__(self):
        return str(self.arr)


if __name__ == "__main__":
    h1 = HashMap()
    h1['march 7'] = 757
    h1['march 27'] = 245
    h1['march 6'] = 235
    h1['march 26'] = 234
    h1['march 14'] = 45
    # print(h1['march 7'])
    h1['march 7']
    # h1['march 27']
    print(h1)
    h1['march 7'] = 257
    h1['march 7']
    h1['march 6']
    h1['march 17']
    h1['may 6'] = 65
    h1['may 6']
    del h1['may 27']
    print(h1)


'''
OUTPUT - 
757
[[('march 7', 757), ('march 27', 245)], [], [], [], [], [], [('march 14', 45)], [], [], [('march 6', 235), ('march 26', 234)]]        
257
235
NOT FOUND !
65
[[('march 7', 257), ('march 27', 245)], [], [], [('may 6', 65)], [], [], [('march 14', 45)], [], [], [('march 6', 235), ('march 26', 234)]]

'''
'''

    def __getitem__(self, key):
        h = self.get_hash(key)  # 6 int
        for i in self.arr[h]:
            if i[0] == key:
                print(i[1])

'''
