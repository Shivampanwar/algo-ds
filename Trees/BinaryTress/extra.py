import sys


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def print_level_helper(root, temp_list):
    if not len(temp_list):
        return
    if not root:
        return
    print("")
    sys.stdout.write(str(root.data) + ":")
    if root.left:
        sys.stdout.write(" " + str(root.left.data))
    else:
        sys.stdout.write(" " + str(-1))
    if root.right:
        sys.stdout.write(" " + str(root.right.data))
    else:
        sys.stdout.write(" " + str(-1))
    if root.left:
        temp_list.append(root.left)
    if root.right:
        temp_list.append(root.right)
    temp_list.pop(0)
    if len(temp_list):
        print_level_helper(temp_list[0], temp_list)
    return


def printLevelWise(root):
    # Given a binary tree, print the tree in level wise order. For printing
    # a node with data N, you need to follow the exact format:
    # N:L:x,R:y
    # wherer, N is data of any node present in the binary tree. x and y are the
    # values of left and right child of node N. Print -1. if any child is null.
    # There is no space in between. You need to print all nodes in the level
    # order form in different lines.
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    temp_list = [root]
    print_level_helper(root, temp_list)


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
inp2 = "1 2 3 -1 -1 -1 -1"
inp = "8 3 10 1 6 1 14 -1 -1 4 7 13 -1 -1 -1 -1 -1 -1 -1"
# inp="8 3 10 -1 -1 4 5 -1 -1 -1 -1"
levelOrder = [int(i) for i in inp2.strip().split()]
# print levelOrder
root = buildLevelTree(levelOrder)
printLevelWise(root)
