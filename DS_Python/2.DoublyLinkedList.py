# Doubly Linked List
# Almost similar to the Linked List
# Just there is a block which points to previous Node


class Node:
    def __init__(self, prev=None, data=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next


class DoublyLinkedList:
    def __init__(self):
        self.head = None   # Linke LL, In DLL head points to None

    def insert_at_beginning(self, data):
        if self.head is None:
            node = Node(None, data, self.head)
            self.head = node
        else:
            node = Node(None, data, self.head)
            self.head.prev = node
            self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.insert_at_beginning(data)

        else:
            itr = self.head
            while itr.next:
                itr = itr.next

            itr.next = Node(itr, data, itr.next)

    def print(self):
        if self.head is None:
            print("Doubly Linked List is empty !")

        else:
            itr = self.head
            llstr = ""
            while itr:
                llstr += str(itr.data)+"--->"
                itr = itr.next

            print(llstr)

    def getlength(self):
        if self.head is None:
            return None

        else:
            count = 0
            itr = self.head
            while itr:
                count += 1
                itr = itr.next
            return count

    def insert_at(self, index, data):
        if index < 0 or index > self.getlength():
            raise Exception("Invalid Index")

        elif index == self.getlength():
            self.insert_at_end(data)

        elif index == 0:
            self.insert_at_beginning(data)

        else:
            count = 0
            itr = self.head
            while itr:
                if count == index-1:
                    # itr points to the previous node
                    itr.next = Node(itr, data, itr.next)
                    break
                count += 1
                itr = itr.next

    def remove_at(self, index):
        if index < 0 or index >= self.getlength():
            raise Exception("Invalid Index")

        elif index == 0:
            self.head = self.head.next

        else:
            count = 0
            itr = self.head
            while itr:
                if count == index-1:
                    itr.next = itr.next.next
                    break
                count += 1
                itr = itr.next

    def insert_in_middle(self, data):
        if self.head is None:
            print("Sorry Cant figure out the middle !")

        else:
            middle = (self.getlength()//2)
            self.insert_at(middle, data)


if __name__ == "__main__":
    d1 = DoublyLinkedList()
    d1.insert_at_beginning(2)
    d1.insert_at_beginning(1)
    d1.insert_at_beginning("START")
    d1.insert_at_end("END")
    d1.insert_at(3, "TWO")
    d1.print()
    d1.remove_at(3)
    d1.insert_in_middle("MIDDLE")
    d1.print()
    print(d1.getlength())
