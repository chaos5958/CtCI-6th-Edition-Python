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

def sum(ll1, ll2):
    ll3 = SinglyLinkedList()
    runner1 = ll1.head
    runner2 = ll2.head
    remainder = 0

    while not (runner1 is None and runner2 is None):
        if runner1 == None:
            ll3.add(runner2.value)
            runner2 = runner2.next
        elif runner2 == None:
            ll3.add(runner1.value)
            runner1 = runner1.next
        else:
            sum_tmp = runner1.value + runner2.value + remainder
            remainder = sum_tmp // 10
            ll3.add(sum_tmp % 10)
            runner1 = runner1.next
            runner2 = runner2.next
    if remainder != 0:
        ll3.add(remainder)

    return ll3

def sum_reverse(ll1, ll2):
    ll3 = SinglyLinkedList()

    len_ll1 = len(ll1)
    len_ll2 = len(ll2)

    if len_ll1 > len_ll2:
        for _ in range(len_ll1 - len_ll2):
            ll2.add_to_beggining(0)
    if len_ll2 > len_ll1:
        for _ in range(len_ll2 - len_ll1):
            ll1.add_to_beggining(0)

    runner1 = ll1.head
    runner2 = ll2.head
    result = 0
    while runner1 and runner2:
        result = result * 10 + runner1.value + runner2.value
        runner1 = runner1.next
        runner2 = runner2.next

    for i in str(result):
        ll3.add(int(i))

    return ll3


ll1 = SinglyLinkedList()
ll2 = SinglyLinkedList()
ll1.add(7)
ll1.add(1)
ll1.add(6)
ll2.add(5)
ll2.add(9)
ll2.add(2)
print(ll1)
print(ll2)
ll3 = sum(ll1, ll2)
print(ll3)

ll1 = SinglyLinkedList()
ll2 = SinglyLinkedList()
ll1.add(6)
ll1.add(1)
ll1.add(7)
ll2.add(2)
ll2.add(9)
ll2.add(5)
print(ll1)
print(ll2)
ll3 = sum_reverse(ll1, ll2)
print(ll3)
