class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = Node('head')
        self.size = 0

    def __str__(self):
        cur = self.head.next
        out = ''
        while cur:
            out += str(cur.value) + '->'
            cur = cur.next
        return out[:-2]

    def getSize(self):
        return self.size

    def pop(self):
        if self.isEmpty():
            raise Exception('empty')
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value

    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def peek(self):
        if self.isEmpty():
            raise Exception('empty')
        return self.head.next.value

    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False

class MyQueue:
    def __init__(self):
        self.stackNewest = Stack()
        self.stackOldest = Stack()

    def getSize(self):
        return self.stackNewest.getSize() + self.stackOldest.getSize()

    def add(self, value):
        self.stackNewest.push(value)

    def shiftStack(self):
        if (self.stackOldest.isEmpty()):
            while not self.stackNewest.isEmpty():
                self.stackOldest.push(self.stackNewest.pop())

    def remove(self):
        self.shiftStack()
        return self.stackOldest.pop()

    def peek(self):
        self.shiftStack()
        return self.stackOldest.peek()

mq = MyQueue()
mq.add(1)
mq.add(2)
mq.add(3)
print(mq.remove())
print(mq.remove())
print(mq.remove())
