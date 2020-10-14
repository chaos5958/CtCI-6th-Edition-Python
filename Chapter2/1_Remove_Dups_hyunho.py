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

    """2.1"""
def remove_dups_with_buffer(ll):
    buf = []
    if ll.head is None:
        return

    current = ll.head
    seen = set([ll.head.value])
    while current.next:
        if current.next.value in seen:
            current.next = current.next.next
        else:
            current = current.next
            seen.add(current.value)

    return ll

def remove_dups_without_buffer(self):
    if ll.head is None:
        return

    refer = ll.head
    while refer.next:
        current = refer
        while current.next:
            if current.next.value == refer.value:
                current.next = current.next.next
            current = current.next
        refer = refer.next
    return ll


"""2.1"""
ll = SinglyLinkedList()
ll.add(100)
ll.add(9)
ll.add(9)
ll.add(100)
ll.add(8)
print(ll)
remove_dups_with_buffer(ll)
print(ll)

ll = SinglyLinkedList()
ll.add(100)
ll.add(9)
ll.add(9)
ll.add(100)
ll.add(8)
print(ll)
remove_dups_without_buffer(ll)
print(ll)
