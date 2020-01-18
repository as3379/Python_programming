class Stack(object):
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self, item): #addes first element
        return self.items.append(item)
    def pop(self): #removes first element
        return self.items.pop()
    def peek(self): #gives top element
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)


s = Stack()
# print(s.isEmpty())
print(s.push(1))
# print(s.isEmpty())
# print(s.pop())
# print(s.isEmpty())
s.push(2)
s.push(3)
# print(s.peek())
print(s.size())
