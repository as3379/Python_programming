

def cycle_cheker(node):
    """ Logic = If linked list is circular marker 1 and marker 2 will meet at some point"""

    marker1 = node
    marker2 = node

    while marker2 != None and marker2.nextnode != None:

        marker1 = marker1.nextnode
        marker2 = marker2.nextnode.nextnode
        if marker1 == marker2:
            return True
    return False


class Node(object):

    def __init__(self, value):
        self.value = value
        self.nextnode = None


a = Node(1)
b = Node(2)
c = Node(3)


a.nextnode = b
b.nextnode = c
c.nextnode = a

print(cycle_cheker(a))
