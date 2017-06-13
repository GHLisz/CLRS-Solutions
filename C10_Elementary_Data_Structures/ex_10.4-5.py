import unittest


class Node:
    def __init__(self, key, p=None, left=None, right=None):
        self.key = key
        self.p = p
        self.left = left
        self.right = right


def print_tree_nonrecursive(node):
    prev = None
    while node is not None:
        if node.p is prev:
            print(node.key)
            prev = node
            if node.left is None:
                node = node.p
            else:
                node = node.left
        elif node.left is prev:
            prev = node
            if node.right is None:
                node = node.p
            else:
                node = node.right
        else:
            prev = node
            node = node.p


class ProblemTestCase(unittest.TestCase):
    def test_case(self):
        head = Node(3, None, Node(1), Node(2))
        head.left.p = head
        head.right.p = head
        print_tree_nonrecursive(head)


if __name__ == '__main__':
    unittest.main()
