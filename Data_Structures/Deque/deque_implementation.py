class Deque(object):
    def __init__(self):
        self.items = []
    def isEmpty(self):
        print(self.items)
        return self.items == []
    def addFront(self, item): #addes to last
        return self.items.append(item)
    def addRear(self, item): #addes first element
        return self.items.insert(0, item)
    def removeFront(self): #removes first element
        return self.items.pop()
    def removeRear(self): #removes last element
        return self.items.pop(0)
    def size(self):
        return len(self.items)


s = Deque()
# print(s.isE

s.addFront('hello')
# print(s.isEmpty())
# print(s.pop())
# print(s.isEmpty())
s.addFront('Ashi')
s.addRear('Gowda')
s.addRear('13')
print(s.isEmpty())
print(s.removeFront())
print(s.removeRear())
