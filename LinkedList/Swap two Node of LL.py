class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def swap_nodes(head, idx1, idx2):
    if idx2 == 0 or idx1 == 0:
        temp = head
        for i in range(max(idx1, idx2) - 1):
            temp = temp.next
        prev = temp
        curr = temp.next
        temp = head
        head = temp.next
        temp.next = curr.next
        prev.next = temp
        curr.next = head
        head = curr
        return head
    # if tail:
    #     pass
    temp = head
    for i in range(idx1 - 1):
        temp = temp.next
    prev1 = temp
    curr1 = temp.next
    temp = head
    for i in range(idx2 - 1):
        temp = temp.next
    prev2 = temp
    curr2 = temp.next
    if not curr2:
        prev1.next = curr2
        curr2.next = curr1.next
        prev2.next = curr1
        curr1.next = None
        return head
    if not curr1:
        prev2.next = curr1
        curr1.next = curr2.next
        prev1.next = curr1
        curr2.next = None
        return head

    prev1.next = curr2
    prev2.next = curr1
    temp_node = curr2.next
    curr2.next = curr1.next
    curr1.next = temp_node
    return head


def ll(arr):
    if len(arr) == 0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head


def pprint(ll):
    temp = ll
    while temp:
        print temp.data
        temp = temp.next


# Main
# Read the link list elements including -1
inp = "3 4 5 2 6 1 9 -1"
arr = list(int(i) for i in inp.strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
l = swap_nodes(l, 2, 4)
pprint(l)
