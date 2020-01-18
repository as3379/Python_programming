class Node(object):

    def __init__(self, value):
        self.value = value
        self.nextnode = None

a = Node(1)
b = Node(2)
c = Node(3)


a.nextnode = b
b.nextnode = c

print(a.nextnode.value, b.nextnode.value)
