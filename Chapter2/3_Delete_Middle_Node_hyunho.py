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

def remove_inter_node(node):
    node.value = node.next.value
    node.next = node.next.next

ll = SinglyLinkedList()
ll.add(1)
ll.add(2)
ll.add(3)
middle_node = ll.add(5)
ll.add(6)
ll.add(7)
ll.add(8)

print(ll)
delete_middle_node(middle_node)
print(ll)
