import unittest


class Node:
    def __init__(self, key, p=None, left=None, right=None):
        self.key = key
        self.p = p
        self.left = left
        self.right = right


def print_tree(node):
    if node is not None:
        print(node.key)
        print_tree(node.left)
        print_tree(node.right)


class ProblemTestCase(unittest.TestCase):
    def test_case(self):
        head = Node(3, None, Node(1), Node(2))
        head.left.p = head
        head.right.p = head
        print_tree(head)


if __name__ == '__main__':
    unittest.main()
