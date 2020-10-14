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

def select_kth_elem_reverse(ll, k):
    former_node = ll.head
    latter_node = ll.head

    for _ in range(k):
        if former_node.next == None:
            return None
        former_node = former_node.next

    while former_node.next:
        latter_node = latter_node.next
        former_node = former_node.next

    return latter_node

ll = SinglyLinkedList()
ll.add(1)
ll.add(2)
ll.add(3)
ll.add(4)
ll.add(5)
ll.add(6)
ll.add(7)
ll.add(8)
ll.add(9)
ll.add(10)
print(ll)
print(select_kth_elem_reverse(ll, 3).value)
print(select_kth_elem_reverse(ll, 7).value)
