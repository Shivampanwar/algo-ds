import sys


class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def __str__(self):
        return str(self.data)


def postOrder(tree):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if not len(tree.children):
        sys.stdout.write(str(tree.data) + " ")
        return
    for i in tree.children:
        postOrder(i)
    sys.stdout.write(str(tree.data) + " ")


def createLevelWiseTree(arr):
    root = treeNode(int(arr[0]))
    q = [root]
    size = len(arr)
    i = 1
    while i < size:
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1
        for j in range(0, childCount):
            temp = treeNode(int(arr[i + j]))
            parent.children.append(temp)
            q.append(temp)
        i += childCount
    return root


# Main
inp = "10 3 20 30 40 2 40 50 0 0 0 0"
arr = list(int(x) for x in inp.strip().split(' '))
tree = createLevelWiseTree(arr)
postOrder(tree)
