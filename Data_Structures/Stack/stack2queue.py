class stack2queue():
    def __init__(self):
        self.instack = []
        self.outstack =[]
    def enqueue(self, item):
        return self.instack.append(item)

    def dequeue(self):
        self.outstack.append(self.instack.pop())
        return self.outstack.pop()

a = stack2queue()
a.enqueue(0)
a.enqueue(1)
a.enqueue(2)
a.enqueue(3)
print(a.enqueue(4))
a.dequeue()
