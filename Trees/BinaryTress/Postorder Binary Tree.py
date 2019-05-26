class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


import sys


def postOrder(root):
    # Given a binary tree, print the postorder traversal of given tree.
    # Post-order traversal is: LeftChild RightChild Root
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if not root:
        return
    postOrder(root.left)
    postOrder(root.right)
    sys.stdout.write(str(root.data) + " ")
    return


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
inp = "1 2 5 3 9 -1 -1 -1 -1 -1 -1"
inp = "1 2  -1 -1 -1 "
inp = "8 3 10 1 6 -1 14 -1 -1 4 7 13 -1 -1 -1 -1 -1 -1 -1"
levelOrder = [int(i) for i in inp.strip().split()]
root = buildLevelTree(levelOrder)
postOrder(root)
