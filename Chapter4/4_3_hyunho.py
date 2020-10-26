from collections import deque

class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data) + ',' + str(self.next)

def tree_to_lists(binary_tree):
    if not binary_tree:
        return []
    array = []
    queue = deque()

    queue.append((binary_tree, 1))
    #bfs
    while len(queue) > 0:
        binary_tree, height = queue.popleft()
        #initial node
        if len(array) < height:
            linked_list = ListNode(binary_tree.data)
            array.append(linked_list)
        #other nodes
        else:
            linked_list = array[height-1]
            while linked_list.next is not None:
                linked_list = linked_list.next
            linked_list.next = ListNode(binary_tree.data)
        if binary_tree.left:
            queue.append((binary_tree.left, height + 1))
        if binary_tree.right:
            queue.append((binary_tree.right, height + 1))

    return array

import unittest

class Test(unittest.TestCase):
    def test_list_of_depths(self):
        node_h = TreeNode('H')
        node_g = TreeNode('G')
        node_f = TreeNode('F')
        node_e = TreeNode('E', node_g)
        node_d = TreeNode('D', node_h)
        node_c = TreeNode('C', None, node_f)
        node_b = TreeNode('B', node_d, node_e)
        node_a = TreeNode('A', node_b, node_c)
        print(str(node_a.left))
        lists = tree_to_lists(node_a)
        self.assertEqual(str(lists[0]), "A,None")
        self.assertEqual(str(lists[1]), "B,C,None")
        self.assertEqual(str(lists[2]), "D,E,F,None")
        self.assertEqual(str(lists[3]), "H,G,None")
        self.assertEqual(len(lists), 4)

if __name__ == "__main__":
    unittest.main()
