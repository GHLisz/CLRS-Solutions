import unittest


class Node:
    def __init__(self, key, p=None, left_child=None, right_sibling=None):
        self.key = key
        self.p = p
        self.left_child = left_child
        self.right_sibling = right_sibling


def print_tree(node):
    if node is not None:
        print(node.key)

    if node.left_child is not None:
        print_tree(node.left_child)

    if node.right_sibling is not None:
        print_tree(node.right_sibling)


class ProblemTestCase(unittest.TestCase):
    def test_case(self):
        root = Node(3)
        node1 = Node(1, root, None, Node(2))
        root.left_child = node1
        print_tree(root)


if __name__ == '__main__':
    unittest.main()
