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


def tree_insert(T, z):
    y = None
    x = T.root
    while x is not None:
        y = x
        x = x.left if z.key < x.key else x.right
    z.p = y
    if y is None:
        T.root = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z
    return T


def to_list(T):
    root = T.root
    if root is None:
        return []
    return to_list(root.left) + [root.key] + to_list(root.right)


class ProblemTestCase(unittest.TestCase):

    def test_case(self):
        root = Tree(root=TreeNode(3))
        # root = tree_insert(None, TreeNode(3))
        root = tree_insert(root, TreeNode(1))
        root = tree_insert(root, TreeNode(5))
        root = tree_insert(root, TreeNode(0))
        root = tree_insert(root, TreeNode(2))
        root = tree_insert(root, TreeNode(4))
        root = tree_insert(root, TreeNode(6))
        self.assertEqual(to_list(root), [0, 1, 2, 3, 4, 5, 6])


if __name__ == '__main__':
    unittest.main()
