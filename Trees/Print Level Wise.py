import sys


class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def __str__(self):
        return str(self.data)


def printLevelWiseTree(tree):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    root = tree
    unvisited = []
    unvisited.extend(root.children)
    sys.stdout.write(str(root.data) + ":")
    count = 0
    for i in unvisited:
        if count == len(unvisited) - 1:
            sys.stdout.write(str(i.data))
        else:
            sys.stdout.write(str(i.data) + ",")
        count += 1
    while len(unvisited) is not 0:
        root = unvisited.pop(0)
        print("")
        sys.stdout.write(str(root.data) + ":")
        count = 0
        for i in root.children:
            if count == len(root.children) - 1:
                sys.stdout.write(str(i.data))
            else:
                sys.stdout.write(str(i.data) + ",")
            count += 1
        unvisited.extend(root.children)


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
inp = "10 3 20 30 40 2 40 50 0 0 0 0 "
arr = list(int(x) for x in inp.strip().split(' '))
tree = createLevelWiseTree(arr)
printLevelWiseTree(tree)
