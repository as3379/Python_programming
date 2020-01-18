class Queue(object):
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self, item): #addes first element
        self.items.insert(0, item)
        return self.items
    def dequeue(self): #removes first element
        return self.items.pop()
    def size(self):
        return len(self.items)


s = Queue()
# print(s.isEmpty())
print(s.enqueue(1))
# print(s.isEmpty())
# print(s.pop())
# print(s.isEmpty())
s.enqueue(2)
s.enqueue(3)
print(s.enqueue(4))
print(s.dequeue())

# print(items)
# print(s.peek())
# print(s.size())
