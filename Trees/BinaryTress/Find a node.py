class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def isNodePresent(root, x):
    # Given a Binary Tree and an integer x, check if node with data x is present
    # in the input binary tree or not. Return True or False.
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if not root:
        return False
    if root.data == x:
        return True
    return isNodePresent(root.left, x) or isNodePresent(root.right, x)


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


# Main
inp = "8 3 10 1 6 -1 14 -1 -1 4 7 13 -1 -1 -1 -1 -1 -1 -1"
inp = "1 3 5 -1 -1 -1 -1"
levelOrder = [int(i) for i in inp.strip().split()]
root = buildLevelTree(levelOrder)
x = 50
present = isNodePresent(root, x)
if present:
    print('true')
else:
    print('false')
