# Stack
# Last IN First OUT

# Eg. Visiting Websites, stack of plates, elevator

from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, *args):
        for i in args:
            self.container.append(i)

    def pop(self):
        self.container.pop()  # this pop unlike list takes no argument

    def peek(self):
        self.container[-1]

    def is_empty(self):
        print(len(self.container) == 0)

    def size(self):
        print(len(self.container))


if __name__ == "__main__":
    n1 = Stack()
    # new = ["NEW", "Mayan", 2, 3, 4]
    # n1.push(*new)
    n1.push("PICHU", "PIKACHU", "RAICHU", "BULBASAUR", "IVYSAUR", "VENOSAUR")
    n1.push("AIRBENDER")
    print(n1.container)
    n1.pop()
    n1.size()
    n1.is_empty()
    print(n1.container)


'''

deque(['PICHU', 'PIKACHU', 'RAICHU', 'BULBASAUR', 'IVYSAUR', 'VENOSAUR', 'AIRBENDER'])
6
False
deque(['PICHU', 'PIKACHU', 'RAICHU', 'BULBASAUR', 'IVYSAUR', 'VENOSAUR'])

'''
