import queue


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


# Link List Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def printll(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()


def sortedLLFromBST(root):
    # Given a BST, convert it into a sorted linked list. Return the head of
    # LL
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if not root:
        return
    results = []
    left_result = sortedLLFromBST(root.left)
    right_result = sortedLLFromBST(root.right)
    if left_result:
        results.extend(left_result)
    results.append(root.data)
    if right_result:
        results.extend(right_result)
    return results


# Main
levelOrder = [8, 5, 10, 2, 6, -1, -1, -1, -1, -1, 7, -1, -1]

root = buildLevelTree(levelOrder)
ll = sortedLLFromBST(root)
print(ll)
# printll(ll)
