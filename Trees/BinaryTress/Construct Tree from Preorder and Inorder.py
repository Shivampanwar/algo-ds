import queue


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def buildTreePreOrder(preorder, inorder):
    if preorder == []:
        return None
    rootVal = preorder[0]
    leftinorder = []
    rightinorder = []
    for i in range(len(inorder)):
        if rootVal == inorder[i]:
            leftinorder = inorder[:i]
            rightinorder = inorder[i + 1:]
            break
    leftpreorder = preorder[1:len(leftinorder) + 1]
    rightpreorder = preorder[len(leftinorder) + 1:]
    left_sub_tree = buildTreePreOrder(leftpreorder, leftinorder)
    right_sub_tree = buildTreePreOrder(rightpreorder, rightinorder)
    root = BinaryTreeNode(rootVal)
    root.left = left_sub_tree
    root.right = right_sub_tree
    return root


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
# n=int(input())
preorder = [1, 2, 4, 5, 6, 7, 3]
inorder = [4, 2, 6, 5, 7, 1, 3]
# preorder = [int(i) for i in input().strip().split()]
# inorder = [int(i) for i in input().strip().split()]
root = buildTreePreOrder(preorder, inorder)
printLevelATNewLine(root)
