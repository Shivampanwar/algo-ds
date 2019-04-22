lass
BinaryTreeNode:


def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None


class BST:

    def __init__(self):
        self.root = None
        self.numNodes = 0

    def printTreeHelper(self, root):
        if root == None:
            return
        print(root.data, end=":")
        if root.left != None:
            print("L:", end='')
            print(root.left.data, end=',')
        if root.right != None:
            print("R:", end='')
            print(root.right.data, end='')
        print()
        self.printTreeHelper(root.left)
        self.printTreeHelper(root.right)

    def printTree(self):
        self.printTreeHelper(self.root)

    def search(self, data):

    # Implement this function here

    def insert(self, data):

    # Implement this function here

    def delete(self, data):

    # Implement this function here

    def count(self):
        return self.numNodes


b = BST()
li = [int(ele) for ele in input().split()]
i = 0
while (i < (len(li))):
    choice = li[i]
    if choice == 1:
        data = li[i + 1]
        b.insert(data)
        i += 2
    elif choice == 2:
        data = li[i + 1]
        b.delete(data)
        i += 2
    elif choice == 3:
        data = li[i + 1]
        ans = b.search(data)
        if ans is True:
            print('true')
        else:
            print('false')
        i += 2
    else:
        b.printTree()
        i += 1
