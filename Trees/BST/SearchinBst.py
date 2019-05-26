import queue


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def searchInBST(root, k):
    # Given a BST and an integer k. Find if the integer k is present in given
    # BST or not. Return the node with data k if it is present, return null
    # otherwise. Assume that BST contains all unique elements.
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if not root:
        return
    else:
        if root.data == k:
            return root
        if root.data > k:
            return searchInBST(root.left, k)
        else:
            return searchInBST(root.right, k)


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


# Main
levelOrder = [8, 5, 10, 2, 6, -1, -1, -1, -1, -1, 7, -1, -1]
root = buildLevelTree(levelOrder)
k = 5
node = searchInBST(root, k)
if node:
    print(node.data)
