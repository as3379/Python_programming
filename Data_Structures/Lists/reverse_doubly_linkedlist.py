# Program to reverse a doubly linked list



class Node():
    # Constructor for empty Doubly Linked List
    def __init__(self,data):

        self.data = data
        self.head = None
        self.next = None
        self.prev = None

    # Function reverse a Doubly Linked List
    def reverse(self):
        temp = None
        current = self.head

        # Swap next and prev for all nodes of
        # doubly linked list
        while current is not None:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev

            # Before changing head, check for the cases like
        # empty list and list with only one node
        if temp is not None:
            self.head = temp.prev

            # Given a reference to the head of a list and an



        # integer,inserts a new node on the front of list
    def push(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur
            new_node.next = None

    def printList(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next


# Driver program to test the above functions
dll = Node(data=None)
dll.push(2)
dll.push(4)
dll.push(8)
dll.push(10)

print("\nOriginal Linked List", dll.printList())

# Reverse doubly linked list
dll.reverse()

print("\n Reversed Linked List", dll.printList())
