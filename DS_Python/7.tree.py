# Tree (General Tree)


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def chil(self):
        if len(self.children) == 0:
            return None
        else:
            final = []
            for child in self.children:
                final.append(child.data)
            return final

    def par(self):
        if self.parent is None:
            return None
        else:
            return str(self.parent.data)

    def getLevel(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def tree(self):
        prefix = "|--->"
        spaces = " "*self.getLevel()
        print(spaces+prefix+str(self.getLevel())+spaces+self.data)
        if self.children:
            for child in self.children:
                child.tree()


def buildTree():
    electronics = TreeNode("Electronics")

    mobile = TreeNode("Mobile")
    laptop = TreeNode("Laptop")
    television = TreeNode("Television")

    iphone = TreeNode("Iphone")
    s10 = TreeNode("S10")
    oneplus = TreeNode("Oneplus")

    hp = TreeNode("HP")
    macbook = TreeNode("Macbook")
    dell = TreeNode("Dell")

    lg = TreeNode("LG")
    sony = TreeNode("Sony")
    toshiba = TreeNode("Toshiba")

######### ELECTRONICS CHILDREN ##############
    electronics.add_child(mobile)
    electronics.add_child(laptop)
    electronics.add_child(television)
######## MOBILE CHILDREN ###################
    mobile.add_child(iphone)
    mobile.add_child(s10)
    mobile.add_child(oneplus)
####### LAPTOP CHILDREN ###################
    laptop.add_child(hp)
    laptop.add_child(macbook)
    laptop.add_child(dell)
####### TELEVISION CHILDREN ###############
    television.add_child(lg)
    television.add_child(sony)
    television.add_child(toshiba)

    # print("Electronics level ---->", electronics.getLevel())
    # print("Mobile,Laptop,Television level ---->", mobile.getLevel())
    # print("iphone,hp,LG etc Level ---->", iphone.getLevel())
    # print(electronics.tree())
    # print(electronics.children)
    return electronics


if __name__ == "__main__":
    root = buildTree()
    print(root.chil())
    root.tree()
