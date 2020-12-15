# HASH MAP (more like dictionary in Python)


class HashMap:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for i in key:
            h += ord(i)
        final = h % self.MAX
        return final

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        self.arr[h] = value

    def __getitem__(self, key):
        h = self.get_hash(key)
        if self.arr[h] == None:
            print("NOT FOUND!")
        else:
            print(self.arr[h])

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None

    def __str__(self):  # Remember in str, only str can be returned not a list
        return str(self.arr)


if __name__ == "__main__":
    h1 = HashMap()
    # h1.get_hash('march 6')
    h1["march 6"] = 323.0
    h1["march 6"]
    h1["march 23"] = 112.0
    h1["January 27"] = 234.0
    h1["march 7"] = 435.0
    print(h1.get_hash("march 7"))
    print(h1)
    del h1["march 6"]
    print(h1)
    h1['may 12']


'''
OUTPUT - 

323.0
[None, None, None, None, None, None, 112.0, 234.0, None, 323.0]
[None, None, None, None, None, None, 112.0, 234.0, None, None]

'''
