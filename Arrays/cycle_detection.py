"""Cycle Detection"""


# Method1:
def floyd(a):
    fast = 0
    slow = 0
    while True:
        if (fast < 0 or slow < 0 or fast >= len(a) or slow >= len(a)):
            return False
        fast = a[fast]
        # if (p == q):
        #     return True
        # if (p<0 or q < 0 or p>=len(a) or q>=len(a)):
        #     return False
        fast = a[fast]
        if (fast == slow):
            return slow
        slow = a[slow]
        if fast == slow:
            return slow


a = [1, 2, 1, 3, 4, 8]

# B = [1,2,3,4,5,6]
# C = [1, 1, 1, 1, 1, 1]
# D = [2, -1, 1, 2, 2]
# print(floyd(a))
slow = floyd(a)


def start(slow, a):
    fast = 0
    while (fast != slow):
        slow = a[slow]
        fast = a[fast]
    return slow


print(start(slow, a))
a = [1, 2, 1, 3, 4, 8]

B = [1, 2, 3, 4, 5, 6]
C = [1, 1, 1, 1, 1, 1]
D = [2, -1, 1, 2, 2]
print(floyd(a))
print(floyd(B))
print(floyd(C))
print(floyd(D))


# Method2:
def has_cycle(head):
    fast = head;

    while (fast != None and fast.next != None):
        fast = fast.next.next;
        head = head.next;

        if (head == fast):
            return True;


