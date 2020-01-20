def reverse(head):
    current = head
    nextnode = None
    previous = None

    while current:
        nextnode = current.nextnode
        current.nextnode  = previous #pointing next node to previous node to reverse elements
        previous = current
        current = nextnode
    return previous


class Node(object):

    def __init__(self, value):
        self.value = value
        self.nextnode = None

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)


a.nextnode = b
b.nextnode = c
c.nextnode = d

print(a.nextnode.value ) #2
print(b.nextnode.value ) #3
print(c.nextnode.value ) #4

reverse(a) # a, b, c, d  >>> d, c, b, a  >>> 4, 3, 2, 1

print(d.nextnode.value ) #3
print(c.nextnode.value ) #2
print(b.nextnode.value ) #1
