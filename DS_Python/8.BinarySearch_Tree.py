class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return None
        elif data < self.data:
            if self.left is None:
                self.left = BSTNode(data)
            else:
                self.left.add_child(data)
        else:
            if self.right is None:
                self.right = BSTNode(data)
            else:
                self.right.add_child(data)

#  Left -- Root -- Right
    def inorder(self):
        elements = []
        # LEFT TREE
        if self.left:
            elements += self.left.inorder()
        # CENTRE ROOT
        elements.append(self.data)
        # RIGHT TREE
        if self.right:
            elements += self.right.inorder()
        return elements

#  Root -- Left -- Right
    def preorder(self):
        elements = []
        elements.append(self.data)
        if self.left:
            elements += self.left.preorder()

        if self.right:
            elements += self.right.preorder()

        return elements

# Left -- Right -- Root
    def postorder(self):
        elements = []
        if self.left:
            elements += self.left.postorder()
        if self.right:
            elements += self.right.postorder()
        elements.append(self.data)

        return elements

    def search(self, value):
        if value == self.data:
            return True
        elif value < self.data:
            if self.left is None:
                return False
            else:
                return self.left.search(value)
        else:
            if self.right is None:
                return False
            else:
                return self.right.search(value)

    def __str__(self):
        return str(self.left.data) + "<----" + str(self.data) + "---->" + str(self.right.data)

        # return (f"{str(self.left.data)}<==={str(self.data)}===>{str(self.right.left)}")
'''
             22
            / \
          12  25  
         / \  / \
        4    23  66 
                 / \ 
                    545
'''

if __name__ == "__main__":
    root = BSTNode(22)
    root.add_child(12)
    root.add_child(25)
    root.add_child(4)
    root.add_child(66)
    root.add_child(23)
    root.add_child(545)
    print(root.inorder())
    print(root)
    print(root.left.data)
    print(root.right.data)
    print(root.preorder())
    print(root.postorder())
    print(root.search(545))
