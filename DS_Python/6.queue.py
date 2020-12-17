# Queue
# First IN First OUT
# Methods - enqueue, dequeue(pop), is_empty,size

from collections import deque


class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, *args):
        for i in args:
            self.buffer.appendleft(i)

    def dequeue(self):
        self.buffer.pop()

    def is_empty(self):
        print(len(self.buffer) == 0)

    def size(self):
        print(len(self.buffer))

    def __str__(self):
        return str(self.buffer)


if __name__ == "__main__":
    q1 = Queue()
    q2 = Queue()
    q2.enqueue(4, 3, 2, 1)
    q1.enqueue({'name': 'BMW', 'model': 'Z1', 'price': 0.80})
    q1.enqueue({'name': 'Mercedes', 'model': 'AMG', 'price': 1.50})
    q1.enqueue({'name': 'Range Rover', 'model': 'Evoque', 'price': 0.60})
    q1.enqueue({'name': 'Jaguar', 'model': 'X1', 'price': 0.70})
    print(q1.buffer)
    q1.is_empty()
    q1.size()
    q1.dequeue()
    print(q1)
    print(q1.buffer)
    print(q2)
    print(q2.dequeue())
    print(q2)


'''
OUTPUT - 

deque([{'name': 'Jaguar', 'model': 'X1', 'price': 0.7}, {'name': 'Range Rover', 'model': 'Evoque', 'price': 0.6}, {'name': 'Mercedes', 'model': 'AMG', 'price': 1.5}, {'name': 'BMW', 'model': 'Z1', 'price': 0.8}])
False
4
deque([{'name': 'Jaguar', 'model': 'X1', 'price': 0.7}, {'name': 'Range Rover', 'model': 'Evoque', 'price': 0.6}, {'name': 'Mercedes', 'model': 'AMG', 'price': 1.5}])
deque([{'name': 'Jaguar', 'model': 'X1', 'price': 0.7}, {'name': 'Range Rover', 'model': 'Evoque', 'price': 0.6}, {'name': 'Mercedes', 'model': 'AMG', 'price': 1.5}])
deque([1, 2, 3, 4])
None
deque([1, 2, 3])


'''
