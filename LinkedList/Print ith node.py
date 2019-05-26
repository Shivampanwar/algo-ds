class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def ithNode(head, i):
    temp = head
    for j in range(i):
        if temp:
            temp = temp.next

        else:
            return None
    return temp


def length(head):
    temp = head
    count = 0
    if temp:
        while temp.next:
            count += 1
            temp = temp.next

        count += 1
    return count


def delete(head, i):
    if i == 0:
        temp = head
        head = temp.next
        del temp
        return head
    else:
        temp = head
        if temp:
            for i in range(1, i):
                if temp:
                    temp = temp.next
                else:
                    return head
        to_delete = temp.next
        if temp.next:
            if temp.next.next:
                temp.next = temp.next.next
                del to_delete
            else:
                temp.next = None
                del to_delete
            return head


def lengthRecursive(head):
    if head:
        return 1 + lengthRecursive(head.next)
    else:
        return 0


def ll(arr):
    if len(arr) == 0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head


def insert_recursive(head, index, node):
    if not head and index > 0:
        return  ##suspicious
    if not head and index == 0:
        return node
    if index == 0:
        temp = head
        head = node
        head.next = temp
        return head
    head.next = insert_recursive(head.next, index - 1, node)
    return head


# Main
# Read the link list elements including -1
# arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll([3, 4, 5, 2, 6, 1, 9])
# print lengthRecursive(l)
# i=100
# node = ithNode(l, i)
# if node:
#     print(node.data)
node = Node(100)
a = insert_recursive(l, 7, node)
print "jds"
temp = a
while temp:
    print temp.data
    temp = temp.next
