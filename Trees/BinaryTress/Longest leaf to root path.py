class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)
    if length <= 0 or levelorder[0] == -1:
        return None
    root = BinaryTreeNode(levelorder[index])
    index += 1
    q = []
    q.append(root)
    while len(q) is not 0:
        currentNode = q.pop(0)
        leftChild = levelorder[index]
        index += 1
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left = leftNode
            q.append(leftNode)
        rightChild = levelorder[index]
        index += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right = rightNode
            q.append(rightNode)
    return root


def longestpath(root):
    if not root:
        return []
    list_left = longestpath(root.left)
    list_right = longestpath(root.right)
    if len(list_left) >= len(list_right):
        list_left.insert(0, root.data)
        return list_left
    else:
        list_right.insert(0, root.data)
        return list_right


def printlevelwise(root):
    q = [root]
    while q:
        main = q[0]
        print
        main.data
        if main.left:
            q.append(main.left)
        if main.right:
            q.append(main.right)
        q.pop(0)


inp = " 5 6 10 2 3 -1 -1 -1 -1 -1 9 -1 -1"
levelOrder = [int(i) for i in inp.strip().split()]
root = buildLevelTree(levelOrder)
print
longestpath(root)
