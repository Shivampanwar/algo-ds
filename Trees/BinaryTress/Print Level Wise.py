import sys


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def print_level_helper(root, temp_list):
    if not len(temp_list):
        return
    sys.stdout.write(str(root.data) + ":")
    sys.stdout.write(str(root.left.data))
    sys.stdout.write(str(root.right.data))
    temp_list.append(root.left)
    temp_list.append(root.right)
    temp_list.pop(0)
    print_level_helper(temp_list[0], temp_list)


def printLevelOrder(root):
    # Base Case
    if root is None:
        return

    # Create an empty queue for level order traversal
    queue = []

    # Enqueue Root and initialize height
    queue.append(root)

    while (len(queue) > 0):
        # Print front of queue and remove it from queue
        print
        queue[0].data,
        node = queue.pop(0)

        # Enqueue left child
        if node.left is not None:
            queue.append(node.left)

            # Enqueue right child
        if node.right is not None:
            queue.append(node.right)


import queue


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
    # print "data"+str(root.data)+root.left
    # temp_list=[root]
    # print_level_helper(root,temp_list)
    if root == None:
        return
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        curr = q.get()
        currData = curr.data
        left = -1
        right = -1
        if curr.left != None:
            left = curr.left.data
            q.put(curr.left)
        if curr.right != None:
            right = curr.right.data
            q.put(curr.right)
        print(currData, ":L:", left, ",R:", right, sep='')


def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)
    if length <= 0 or levelorder[0] == -1:
        return None
    root = BinaryTreeNode(levelorder[index])
    index += 1
    q = []
    q.append(root)
    while not len(q):
        currentNode = q.pop()
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
# inp="8 3 10 1 6 -1 14 -1 -1 4 7 13 -1 -1 -1 -1 -1 -1 -1"
inp = "8 3 10 -1 -1 -1 -1"
levelOrder = [int(i) for i in inp.strip().split()]
print(levelOrder)
root = buildLevelTree(levelOrder)
printLevelOrder(root)
