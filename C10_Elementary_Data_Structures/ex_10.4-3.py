import unittest


class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self):
        self.root = None


def print_tree(node):
    stack = [node, ]
    while len(stack) > 0:
        node = stack.pop()
        if node is not None:
            print(node.key)
            stack.append(node.left)
            stack.append(node.right)


class ProblemTestCase(unittest.TestCase):
    def test_case(self):
        head = Node(3, Node(1), Node(2))
        print_tree(head)


if __name__ == '__main__':
    unittest.main()
