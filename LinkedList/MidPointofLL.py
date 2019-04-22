# Problem ID 328 Midpoint LL
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def find_length(head):
    count = 0
    temp = head
    while temp.next:
        count += 1
        temp = temp.next
    count += 1
    return count


def midpoint_linkedlist(head):
    #  Given a linked list, find and return the midpoint.
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    length = find_length(head)
    if length % 2 == 0:
        length += -1
    mid = length / 2
    temp = head
    for i in range(mid):
        temp = temp.next

    return temp


def ll(arr):
    if len(arr) == 0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head


# Main
# Read the link list elements including -1
inp = "1 2 3 5 7 9 -1"
arr = list(int(i) for i in inp.strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
# print find_length(l)
node = midpoint_linkedlist(l)
if node:
    print(node.data)
