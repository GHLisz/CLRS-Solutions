import random
import unittest


class TreeNode:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.p = None
        self.left = left
        self.right = right
        if left is not None:
            left.p = self
        if right is not None:
            right.p = self


def tree_search(x, k):
    if x is None or x.key == k:
        return x
    if x.key > k:
        return tree_search(x.left, k)
    else:
        return tree_search(x.right, k)


def iterative_tree_search(x, k):
    while x is not None and x.key != k:
        x = x.left if x.key > k else x.right
    return x


def tree_minimum(x):
    while x.left is not None:
        x = x.left
    return x


def tree_maximum(x):
    while x.right is not None:
        x = x.right
    return x


def tree_successor(x):
    if x.right is not None:
        return tree_minimum(x.right)
    y = x.p
    while y is not None and y.right == x:
        x = y
        y = y.p
    return y


def tree_predecessor(x):
    if x.left is not None:
        return tree_maximum(x.left)
    y = x.p
    while y is not None and y.left == x:
        x = y
        y = y.p
    return y


class ProblemTestCase(unittest.TestCase):

    def test_case(self):
        root = TreeNode(3,
                        TreeNode(1, TreeNode(0), TreeNode(2)),
                        TreeNode(5, TreeNode(4), TreeNode(6)))
        self.assertEqual(tree_predecessor(root.left.left), None)
        self.assertEqual(tree_predecessor(root.left), root.left.left)
        self.assertEqual(tree_predecessor(root.left.right), root.left)
        self.assertEqual(tree_predecessor(root), root.left.right)
        self.assertEqual(tree_predecessor(root.right.left), root)
        self.assertEqual(tree_predecessor(root.right), root.right.left)
        self.assertEqual(tree_predecessor(root.right.right), root.right)


if __name__ == '__main__':
    unittest.main()
