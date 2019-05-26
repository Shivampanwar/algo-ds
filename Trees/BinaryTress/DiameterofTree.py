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


def find_diameter(root):
    if not root:
        return
    if not root.left and not root.right:
        return 0, 0
    h = 0
    d_left = 0
    d_right = 0
    h_left = 0
    h_right = 0
    val_left = find_diameter(root.left)
    val_right = find_diameter(root.right)
    if val_left:
        h += val_left[1] + 1
        h_left = val_left[1]
        d_left = val_left[0]
    if val_right:
        h += val_right[1] + 1
        h_right = val_right[1]
        d_right = val_right[0]
    return max(h, d_right, d_left), max(h_left, h_right) + 1


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


inp = " 5 6 10 2 3 -1 -1 -1 -1 -1 -1"
levelOrder = [int(i) for i in inp.strip().split()]
root = buildLevelTree(levelOrder)
print
find_diameter(root)
