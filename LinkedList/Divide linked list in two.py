class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def divide_list(head):
    insert_first = True
    head1 = head
    head2 = head.next
    head = head.next.next
    head1.next = None
    head2.next = None
    while head is not None:
        temp = head.next
        head.next = None
        if insert_first:
            head.next = head1
            head1 = head
            head = temp
            insert_first = False
        else:
            head.next = head2
            head2 = head
            head = temp
            insert_first = True
    return head1, head2


def ll(arr):
    if len(arr) == 0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head


def printll(head):
    while head:
        print(head.data)
        head = head.next
    print()


# Main
# Read the link list elements including -1
inp = " 8 2 5 9 1 4 3 7 -1"
arr = list(int(i) for i in inp.strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
# printll(l)
# i=int(input())
l1, l2 = divide_list(l)
printll(l1)
printll(l2)
