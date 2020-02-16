class Node(object):

    def __init__(self, value):
        self.value = value
        self.nextnode = None
        self.previous = None

a = Node(1)
b = Node(2)
c = Node(3)


a.nextnode = b
b.previous = a
b.nextnode = c
c.previous = b

print(b.previous.value, b.nextnode.value)
