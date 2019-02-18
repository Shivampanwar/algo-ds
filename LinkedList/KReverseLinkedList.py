class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def kReverse(head, n):
    #  Implement kReverse( k ) in a linked list i.e. you need to reverse
    #  first K elements then reverse next k elements and join the linked list and
    #  so on. Indexing starts from 0. If less than k elements left in the last,
    #  you need to reverse them as well. If k is greater than length of LL,
    #  reverse the complete LL. If n is 4 and LL is:
    #  Input: 1 2 3 4 5 6 7 8 9 10
    #  Output: 4 3 2 1 8 7 6 5 10 9
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if not head:
        return None
    else:
        curr = head
        for i in range(n - 1):
            if curr.next:
                curr = curr.next
            else:
                curr = curr.next
                return Reverse(head)
        temp_head = curr.next
        small_output = kReverse(temp_head, n)
        curr.next = None
        current_result = Reverse(head)
        small_head = current_result
        while small_head.next:
            small_head = small_head.next
        # print "data+{}".format(small_head.data)
        small_head.next = small_output
        return current_result


def Reverse(head):
    if not head.next:
        return head
    prev = head
    curr = prev.next
    next = curr.next
    head.next = None
    while next:
        curr.next = prev
        prev = curr
        curr = next
        next = next.next
    curr.next = prev
    head = curr
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


def printll(head):
    while head:
        print(head.data)
        head = head.next
    print()


# Main
# Read the link list elements including -1
inp = "1 2 3 4 5 6 -1"
arr = list(int(i) for i in inp.strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
# printll(l)
# i=int(input())
l = kReverse(l, 4)
# l=Reverse(l)
printll(l)
