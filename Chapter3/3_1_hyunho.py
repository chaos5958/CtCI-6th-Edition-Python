class MultiStack:
    def __init__(self, stack_num, stack_size):
        self.arr = [None for _ in range(stack_num * stack_size)]
        self.num = [0 for _ in range(stack_num)]
        self.stack_num = stack_num
        self.stack_size = stack_size

    def push(self, value, stack_index):
        if self.isFull(stack_index):
            raise Exception("stack is full")
        self.arr[self.num[stack_index] * self.stack_num + stack_index] = value
        self.num[stack_index] += 1

    def pop(self, stack_index):
        if self.isEmpty(stack_index):
            raise Exception("stack is empty")
        value = self.arr[(self.num[stack_index] - 1) * self.stack_num + stack_index]
        self.arr[(self.num[stack_index] - 1) * self.stack_num + stack_index] = None
        self.num[stack_index] -= 1

        return value

    def peek(self, stack_index):
        return self.arr[(self.num[stack_index] - 1) * self.stack_num + stack_index]

    def isFull(self, stack_index):
        if self.num[stack_index] == self.stack_size:
            return True
        else:
            return False

    def isEmpty(self, stack_index):
        if self.num[stack_index] == 0:
            return True
        else:
            return False

newstack = MultiStack(3, 2)
print(newstack.isEmpty(1))
newstack.push(3, 1)
print(newstack.peek(1))
print(newstack.isEmpty(1))
newstack.push(2, 1)
print(newstack.peek(1))
print(newstack.pop(1))
print(newstack.peek(1))
newstack.push(3, 1)
