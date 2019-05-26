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


#
# def node_max_sum(tree,temp_node=None,value=0):
#     if not len(tree.children):
#         return
#     root=tree
#     temp_value=root.data
#     for i in root.children:
#         temp_value+=i.data
#     if temp_value>value:
#         temp_node=root
#         value=temp_value
#     for i in root.children:
#         node_max_sum(i,temp_node,value)
#     print temp_node.data,value


def node_max_sum(tree):
    if not len(tree.children):
        return tree, tree.data
    main_node = tree
    ans = tree.data
    for i in tree.children:
        ans += i.data
    for i in tree.children:
        node, val = node_max_sum(i)
        if ans < val:
            main_node = node
            ans = val
    return main_node, ans


# Main
inp = "10 3 20 30 40 2 40 50 0 0 0 0"
arr = list(int(x) for x in inp.strip().split(' '))
temp_node = treeNode(0)
tree = createLevelWiseTree(arr)
a, b = node_max_sum(tree)
print
a.data, b
