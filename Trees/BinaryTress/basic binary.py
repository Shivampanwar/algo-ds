class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = root

    def print_tree(self, node):
        if node:
            print
            node.data
            self.print_tree(node.left)
            self.print_tree(node.right)


root = Node(1)
tree = BinaryTree(root)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.print_tree(root)

# Test search
