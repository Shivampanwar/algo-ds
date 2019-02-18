class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def check_palindrome(head):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if not head:
        return True
    if not head.next:
        return True
    mini_tail = head
    while mini_tail.next.next:
        mini_tail = mini_tail.next
    if mini_tail.next.data == head.data:
        mini_tail.next = None
        return check_palindrome(head.next)
    else:
        return False


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
inp = "0 2 3 2 5 -1"
arr = list(int(i) for i in inp.strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
ans = check_palindrome(l)
if ans:
    print("true")
else:
    print("false")
