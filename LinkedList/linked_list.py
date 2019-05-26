class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        if self.head:
            ptr = self.head
            while ptr.next:
                ptr = ptr.next
            ptr.next = new_element
        else:
            self.head = new_element

    def print_ll(self):
        if self.head:
            ptr = self.head
            while ptr.next:
                print ptr.value
                ptr = ptr.next
            print ptr.value


e1 = Element(2)
e2 = Element(3)
e3 = Element(5)
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)
ll.print_ll()
