class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_children(self, obj):
        self.children.append(obj)


def print_children(root):
    print
    root.data
    for i in root.children:
        # print i.data
        print_children(i)


root = Node(2)
p = Node(3)
q = Node(4)
r = Node(5)
s = Node(6)
root.add_children(p)
root.add_children(q)
q.add_children(r)
q.add_children(s)
print_children(root)
