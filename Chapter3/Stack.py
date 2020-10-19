#Python library
from collections import deque

stack = deque()

stack.append('a')
stack.append('b')
stack.append('c')
print(len(stack))
print(stack.pop())
print(len(stack))
print(stack.pop())
print(len(stack))
print(stack.pop())


#Custom implementation


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




if __name__ == '__main__':
    stack = Stack()
    for i in range(1, 11):
        stack.push(i)
    print(f"Stack: {stack}")

    for _ in range(1, 6):
        remove = stack.pop()
        print(f"Pop: {remove}")
    print(f"Stack: {stack}")
