class Element(object):
    def __init__(self,value):
        self.value=value
        self.next=None
class LinkedList(object):
    def __init__(self,head=None):
        self.head=head
    def append(self,element):
        if self.head:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=element
        else:
            self.head=element
    def show_first(self):
        if self.head:
            temp=self.head
            if temp.next:
                self.head=temp.next
                temp.next=None
                return temp.value
            else:
                val=self.head.value
                self.head=None
                return val
        else:
            return None

class Queue:
    def __init__(self, top=None):
        self.ll=LinkedList(top)
    def enqueue(self, new_element):
        self.ll.append(new_element)

    # def peek(self):
    #     if self.ll.head:
    #         return self.ll.head.value
    #     else:
    #         return None

    def dequeue(self):
        return self.ll.show_first()


e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)
# Setup
q = Queue(e1)
q.enqueue(e2)
q.enqueue(e3)

# Test peek
# Should be 1

# Test dequeue
# Should be 1
print q.dequeue()

# Test enqueue
q.enqueue(e4)
# Should be 2
print q.dequeue()
# Should be 3
print q.dequeue()
# Should be 4
print q.dequeue()

# Should be 5
print q.dequeue()