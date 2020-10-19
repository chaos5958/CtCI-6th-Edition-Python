
class MultiStack:
    def __init__(self, stack_size):
        self.arr = [None for _ in range(stack_size)]
        self.num = 0
        self.stack_size = stack_size
        self.min_value = [None for _  in range(stack_size)]

    def push(self, value):
        if self.isFull():
            raise Exception("stack is full")
        self.arr[self.num] = value
        self.num += 1

        if self.num - 1 == 0:
            self.min_value[self.num - 1] = value
        elif value < self.min_value[self.num - 2]:
            self.min_value[self.num - 1] = value
        else:
            self.min_value[self.num - 1] = self.min_value[self.num - 2]


    def pop(self):
        if self.isEmpty():
            raise Exception("stack is empty")
        value = self.arr[self.num - 1]
        self.arr[self.num - 1] = None
        self.num -= 1

        return value

    def peek(self):
        return self.arr[self.num - 1]

    def isFull(self):
        if self.num == self.stack_size:
            return True
        else:
            return False

    def isEmpty(self):
        if self.num == 0:
            return True
        else:
            return False

    def min(self):
        return self.min_value[self.num - 1]

newstack = MultiStack(10)
newstack.push(5)
newstack.push(6)
newstack.push(2)
newstack.push(7)
newstack.push(14)
newstack.push(3)
print(newstack.min())
newstack.push(1)
newstack.push(4)
newstack.push(44)
newstack.push(2)
print(newstack.min())
