def last_nth_node (head, n):

    left = head
    right = head


    for i in range(n-1):
        # Edge_case
        if not right.nextnode:
            raise LookupError('Error n is larger than linked list')
        right = right.nextnode


    while right.nextnode:
        left = left.nextnode
        right = right.nextnode


    return left.value


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


print(last_nth_node (a, 1))
