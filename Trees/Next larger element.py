class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def __str__(self):
        return str(self.data)


def next_larger(tree, n):
    root = tree
    if not len(root.children):
        if root.data > n:
            return root.data
        else:
            return None
    temp_list = []
    for i in root.children:
        val = next_larger(i, n)
        if val:
            temp_list.append(val)
    if root.data > n:
        temp_list.append(root.data)
    if not len(temp_list):
        return
    return min(temp_list)


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
print
next_larger(tree, 18)
