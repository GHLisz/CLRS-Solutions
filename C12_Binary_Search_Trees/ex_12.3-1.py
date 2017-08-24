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


class Tree:
    def __init__(self, root=None):
        self.root = root


def tree_insert(root, z):
    if root is None:
        return z
    if z.key < root.key:
        root.left = tree_insert(root.left, z)
        root.left.p = root
    elif z.key > root.key:
        root.right = tree_insert(root.right, z)
        root.right.p = root
    return root


def to_list(root):
    if root is None:
        return []
    return to_list(root.left) + [root.key] + to_list(root.right)


class ProblemTestCase(unittest.TestCase):

    def test_case(self):
        T = tree_insert(None, TreeNode(3))
        T = tree_insert(T, TreeNode(1))
        T = tree_insert(T, TreeNode(5))
        T = tree_insert(T, TreeNode(0))
        T = tree_insert(T, TreeNode(2))
        T = tree_insert(T, TreeNode(4))
        T = tree_insert(T, TreeNode(6))
        self.assertEqual(to_list(T), [0, 1, 2, 3, 4, 5, 6])


if __name__ == '__main__':
    unittest.main()
