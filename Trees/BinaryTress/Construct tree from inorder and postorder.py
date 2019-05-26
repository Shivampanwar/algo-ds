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


def mirror(root):
    if not root:
        return
    if root.left or root.right:
        root.left, root.right = root.right, root.left
        mirror(root.left)
        mirror(root.right)


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


def maketree(inorder, postorder):
    if not postorder:
        return
    root = BinaryTreeNode(postorder[-1])
    idx_inorder = inorder.index(root.data)
    inorder_left = inorder[:idx_inorder]
    num_inorder_right = len(postorder) - 1 - len(inorder_left)
    inorder_right = inorder[idx_inorder + 1:idx_inorder + num_inorder_right + 1]
    postorder_left = postorder[:len(inorder_left)]
    postorder_right = postorder[len(inorder_left):-1]
    root.left = maketree(inorder_left, postorder_left)
    root.right = maketree(inorder_right, postorder_right)
    return root


# inp="8 3 10 1 6 -1 14 -1 -1 4 7 13 -1 -1 -1 -1 -1 -1 -1"
# inp="1 3 5 -1 -1 -1 -1"
# levelOrder = [int(i) for i in inp.strip().split()]
# root = buildLevelTree(levelOrder)
In = [4, 8, 2, 5, 1, 6, 3, 7]
post = [8, 4, 5, 2, 6, 7, 3, 1]
tree = maketree(In, post)
printlevelwise(tree)
