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


def transplant(T, u, v):
    if u.p is None:
        T.root = v
    elif u is u.p.left:
        u.p.left = v
    else:
        u.p.right = v
    if v is not None:
        v.p = u.p


def tree_delete(T, z):
    if z.left is None:
        transplant(T, z, z.right)
    elif z.right is None:
        transplant(T, z, z.left)
    else:
        y = tree_minimum(z.right)
        if y.p is not z:
            transplant(T, y, y.right)
            y.right = z.right
            y.right.p = y
        transplant(T, z, y)
        y.left = z.left
        y.left.p = y


def tree_minimum(x):
    while x.left is not None:
        x = x.left
    return x


def tree_maximum(x):
    while x.right is not None:
        x = x.right
    return x


def to_list(root):
    if root is None:
        return []
    return to_list(root.left) + [root.key] + to_list(root.right)


class ProblemTestCase(unittest.TestCase):

    def test_case(self):
        T = tree_insert(Tree(), TreeNode(3))
        T = tree_insert(T, TreeNode(1))
        T = tree_insert(T, TreeNode(5))
        T = tree_insert(T, TreeNode(0))
        T = tree_insert(T, TreeNode(2))
        T = tree_insert(T, TreeNode(4))
        T = tree_insert(T, TreeNode(6))
        self.assertEqual(to_list(T.root), [0, 1, 2, 3, 4, 5, 6])
        tree_delete(T, T.root.left)
        self.assertEqual(to_list(T.root), [0, 2, 3, 4, 5, 6])


if __name__ == '__main__':
    unittest.main()
