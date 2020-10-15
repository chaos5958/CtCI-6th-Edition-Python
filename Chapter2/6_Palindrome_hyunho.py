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

def is_palindrome(ll):
    ll_reverse = SinglyLinkedList()
    runner = ll.head

    while runner:
        ll_reverse.add_to_beginning(runner.value)
        runner = runner.next

    runner1 = ll.head
    runner2 = ll_reverse.head

    while runner1 and runner2:
        if runner1.value != runner2.value:
            return False

        runner1 = runner1.next
        runner2 = runner2.next

    return True

ll_true = SinglyLinkedList()
ll_true.add_multiple([1, 2, 3, 4, 5, 4, 3, 2, 1])
print(is_palindrome(ll_true))
ll_false = SinglyLinkedList()
ll_false.add_multiple([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(is_palindrome(ll_false))
