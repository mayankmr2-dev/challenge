# Linked List

# Remember
# itr = self.head ----> current node  (head points to current node)
# itr.next -----------> next node (next points to next node)


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None   # head points to None (intially)

    def insert_at_beginning(self, data):
        # new node with data and pointing where earlier head was pointing
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked List is empty !")

        else:
            itr = self.head  # iterating from head which points to first node
            llstr = ""
            while itr:
                llstr += str(itr.data)+"---->"
                itr = itr.next  # next node address is in next, so moving forward

            print(llstr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
        else:
            itr = self.head
            while itr.next:  # We have to iterate till itr.next is None
                itr = itr.next
            # Once itr.next is None, then
            itr.next = Node(data, None)  # itr.next points to a new node

    def get_length(self):
        if self.head is None:
            return None       # As head points to No Node
        else:
            count = 0
            itr = self.head
            while itr:
                count += 1
                itr = itr.next  # it iterates till there is next then shifts and returns count
            return count

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")

        elif index == 0:
            self.insert_at_beginning(data)

        elif index == self.get_length():
            self.insert_at_end(data)

        else:
            count = 0
            itr = self.head
            while itr:
                if count == index-1:
                    itr.next = Node(data, itr.next)
                    break
                count += 1
                itr = itr.next

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
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

    def in_Middle(self, data):
        if self.head is None:
            print("Cant insert in the middle !")

        else:
            middle_index = (self.get_length())//2
            self.insert_at(middle_index, data)


if __name__ == "__main__":
    l1 = LinkedList()
    l1.insert_at_beginning(22)
    l1.insert_at_beginning(21)
    l1.insert_at_beginning(20)
    l1.insert_at_end("END")
    l1.insert_at_beginning("START")
    l1.insert_at_beginning("NOW")
    l1.print()
    # print(l1.get_length())
    # l1.insert_at(6, "ONE")
    # l1.print()
    l1.in_Middle("MIDDLE_EARTH")
    l1.print()
    l2 = LinkedList()
    l2.insert_at_beginning("ONE")
    l2.insert_at_end("TWO")
    l2.insert_at_end("THREE")
    l2.insert_at_beginning("NOW")
    l2.print()
    l2.remove_at(3)
    l2.print()
