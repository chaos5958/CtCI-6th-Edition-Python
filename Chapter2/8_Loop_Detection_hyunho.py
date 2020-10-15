
class Node:
    def __init__(self, value, nextNode=None, prevNode=None):
        self.value = value
        self.next = None
        self.prev = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def __len__(self):
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next
        return result

    def __str__(self):
        values = [str(x.value) for x in self]
        return ' -> '.join(values)

    def add(self, value):
        if self.head == None:
            self.head = self.tail = Node(value)
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail

    def add_to_beginning(self, value):
        node = Node(value)
        if self.head is None:
            self.tail = self.head = node
        else:
            node.next = self.head
            self.head = node
        return self.head

    def add_multiple(self, values):
        for v in values:
            self.add(v)

#Space: O(n), Time(O(n))
def find_loop(ll):
    runner = ll.head
    seen = set()

    while runner:
        if runner in seen:
            return runner
        seen.add(runner)
        runner = runner.next

    return None

#Space: O(1), Time(O(1))
def find_loop_fast(ll):
    slow = fast = ll.head

    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            break

    if fast.next is None or fast.next.next is None:
        return None

    slow = ll.head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return fast

ll = SinglyLinkedList()
ll.add(1)
ll.add(2)
ll.add(3)
ll.add(4)
ll.tail.next = ll.head
node = Node(5)
node.next = ll.head
ll.head = node

print(find_loop_fast(ll).value)
