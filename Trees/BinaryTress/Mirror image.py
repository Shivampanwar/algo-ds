import queue


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def mirrorBinaryTree(root):
    # Mirror the given binary tree. That is, right child of every nodes should
    # become left and left should become right.
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if not root:
        return
    temp = root.left
    root.left = root.right
    root.right = temp
    mirrorBinaryTree(root.left)
    mirrorBinaryTree(root.right)


def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)
    if length <= 0 or levelorder[0] == -1:
        return None
    root = BinaryTreeNode(levelorder[index])
    index += 1
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)
        rightChild = levelorder[index]
        index += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right = rightNode
            q.put(rightNode)
    return root


# Problem ID 353, Level order traversal
def printLevelATNewLine(root):
    # Given a binary tree, print the level order traversal. Make sure each level
    # start in new line.
    if root == None:
        return
    inputQ = queue.Queue()
    outputQ = queue.Queue()
    inputQ.put(root)
    while not inputQ.empty():
        while not inputQ.empty():
            curr = inputQ.get()
            print(curr.data, end=' ')
            if curr.left != None:
                outputQ.put(curr.left)
            if curr.right != None:
                outputQ.put(curr.right)
        print()
        inputQ, outputQ = outputQ, inputQ


# Main
inp = "1 2 3 4 5 6 7 -1 -1 -1 -1 -1 -1 -1 -1"
levelOrder = [int(i) for i in inp.strip().split()]
root = buildLevelTree(levelOrder)
mirrorBinaryTree(root)
printLevelATNewLine(root)
