from collections import deque
import unittest

class SetOfStacks:
    def __init__(self, max_plates):
        self.stacks = []
        self.num_stacks = 0
        self.max_plates = max_plates

    def push(self, value):
        if self.num_stacks == 0:
            self.stacks.append(deque())
            self.num_stacks += 1
            self.stacks[self.num_stacks - 1].append(value)
        elif len(self.stacks[self.num_stacks - 1]) == self.max_plates:
            self.stacks.append(deque())
            self.num_stacks += 1
            self.stacks[self.num_stacks - 1].append(value)
        else:
            self.stacks[self.num_stacks - 1].append(value)

    def pop(self):
        if len(self.stacks) == 0:
            raise Exception('no stacks')
        value = self.stacks[self.num_stacks - 1].pop()
        if len(self.stacks[self.num_stacks - 1]) == 0:
            del self.stacks[self.num_stacks - 1]
            self.num_stacks -= 1
        return value

    def pop_at(self, stack_index):
        if stack_index > self.num_stacks - 1:
            raise Exception('invalid index')
        elif stack_index == self.num_stacks -1:
            value = self.stacks[stack_index].pop()
            if len(self.stacks[stack_index]) == 0:
                del self.stacks[stack_index]
        else:
            value = self.stacks[stack_index].pop()
            self.left_shift(stack_index + 1)
        return value

    def left_shift(self, stack_index):
        value = self.stacks[stack_index].popleft()
        self.stacks[stack_index - 1].append(value)

        if stack_index == self.num_stacks - 1:
            if len(self.stacks[stack_index]) == 0:
                del self.stacks[stack_index]
                self.num_stacks -= 1
        else:
            self.left_shift(stack_index + 1)

class Tests(unittest.TestCase):
    def test_stacks(self):
        stacks = SetOfStacks(5)
        for i in range(35):
            stacks.push(i)
        lst = []
        for _ in range(35):
            lst.append(stacks.pop())
        self.assertEqual(lst, list(reversed(range(35))))

    def test_pop_at(self):
        stacks = SetOfStacks(5)
        for i in range(35):
            stacks.push(i)
        lst = []
        for _ in range(31):
            lst.append(stacks.pop_at(0))
        self.assertEqual(lst, list(range(4, 35)))

if __name__ == '__main__':
    unittest.main()
