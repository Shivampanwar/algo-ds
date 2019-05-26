class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def __str__(self):
        return str(self.data)


def height(tree):
    if not len(tree.children):
        return 1
    count = 0
    for i in tree.children:
        h = height(i)
        if count < h:
            count = h
    return count + 1


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
# arr = list(int(x) for x in input().strip().split(' '))
inp = "10 9 4 -1 -1 5 8 -1 6 -1 -1 3 -1 -1 -1"
# inp="1 2 3 -1 -1 -1 -1"
arr = list(int(x) for x in inp.strip().split(' '))
tree = createLevelWiseTree(arr)
print(height(tree))
