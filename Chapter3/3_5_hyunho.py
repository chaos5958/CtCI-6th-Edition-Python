
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

#wrong
def sort(stack):
    stack_ = Stack()

    while not stack.isEmpty():
        tmp = stack.pop()
        if not stack_.isEmpty() and tmp < stack_.peek():
            while not stack_.isEmpty():
                if tmp >= stack_.peek():
                    break
                else:
                    stack.push(stack_.pop())
        stack_.push(tmp)

    while not stack_.isEmpty():
        stack.push(stack_.pop())

st = Stack()
st.push(1)
st.push(4)
st.push(2)
st.push(6)

print(st)
sort(st)
print(st)
