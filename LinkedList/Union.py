class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# def Union(head1,head2):
#     temp=head2
#     while temp.next is not None:
#         head2=temp.next
#         temp.next=None
#         temp1=head1
#         while temp1.next is not None:
#             if temp1.data==temp.data:
#                 break
#             temp1=temp1.next
#         temp1.next=temp
#         temp=head2
#     return head1
def insert_at_end(head, node):
    temp = head
    while temp.next:
        if temp.data == node.data:
            return head
        temp = temp.next
    if temp.data == node.data:
        return head
    temp.next = node
    return head
def Union(head1, head2):
    while head2:
        temp = head2
        head2 = temp.next
        temp.next = None
        head1 = insert_at_end(head1, temp)
    return head1


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
inp1 = "1 2 -1"
inp2 = "5 2 1 13 15 -1"
arr = list(int(i) for i in inp1.strip().split(' '))
arr2 = list(int(i) for i in inp2.strip().split(' '))

# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
m = ll(arr2[:-1])
# l = Union(l, m)
# l=insert_at_end(l,Node(1))
l = Union(l, m)
printll(l)
