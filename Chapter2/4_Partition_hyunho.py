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

def partition(ll, value):
    runner_node = ll.head

    while runner_node.next:
        if runner_node.next.value < value:
            ll.add_to_beginning(runner_node.next.value)
            runner_node.next = runner_node.next.next
        else:
            runner_node = runner_node.next

ll = SinglyLinkedList()

ll.add(3)
ll.add(5)
ll.add(8)
ll.add(5)
ll.add(10)
ll.add(2)
ll.add(1)
print(ll)
partition(ll, 5)
print(ll)
