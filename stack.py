
class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def insert_first(self, new_element):
        "Insert new element as the head of the LinkedList"
        new_element.next=self.head
        self.head=new_element
    def delete_first(self):
        "Delete the first (head) element in the LinkedList as return it"
        temp=self.head
        self.head=temp.next
        temp.next=None
        return temp



class Stack(object):
    def __init__(self, top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        "Push (add) a new element onto the top of the stack"
        self.ll.append(new_element)
    def pop(self):
        "Pop (remove) the first element off the top of the stack and return it"
        if self.ll.head:
            temp=self.ll.head
            if temp.next:
                while temp.next.next:
                    temp=temp.next
                tail=temp.next
                temp.next=None
                return tail
            else:
                self.ll.head=None
                return temp
        else:
            return None
# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a Stack
stack = Stack(e1)

# Test stack functionality
stack.push(e2)
stack.push(e3)
print stack.pop().value
print stack.pop().value
print stack.pop().value
print stack.pop()
stack.push(e4)
print stack.pop().value