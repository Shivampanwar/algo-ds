class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def __str__(self):
        return str(self.data)


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


def node_second_smallest(tree):
    if not len(tree.children):
        return [tree.data]
    values = [tree.data]
    for i in tree.children:
        values.extend(node_second_smallest(i))
    values = list(set(values))
    values.sort()
    return values[-2:]


def node_second_smallest2(tree):
    if not len(tree.children):
        return [tree.data]
    values = [tree.data]
    for i in tree.children:
        values.append(i.data)
    values = list(set(values)).sort()
    first_largest = values[-1]
    second_largest = values[-2]
    for i in tree.children:
        fl, sl = node_second_smallest2(i)
        if first_largest > fl:
            if second_largest > sl:
                pass
            else:
                second_largest = sl
        else:
            temp = first_largest
            first_largest = second_largest
            second_largest = max(temp, second_largest)
    return first_largest, second_largest


# Main
inp = "10 3 20 30 40 2 40 50 0 0 0 0"
arr = list(int(x) for x in inp.strip().split(' '))
temp_node = treeNode(0)
tree = createLevelWiseTree(arr)
print
min(node_second_smallest(tree))
print
node_second_smallest(tree)
