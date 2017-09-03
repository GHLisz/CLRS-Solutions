import random
import unittest


class TreeNode:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.succ = None
        self.left = left
        self.right = right
        if left is not None:
            left.p = self
        if right is not None:
            right.p = self


class Tree:
    def __init__(self, root=None):
        self.root = root


def tree_delete(T, z):
    if not z.left:
        transplant(T, z, z.right)
    elif not z.right:
        transplant(T, z, z.left)
    else:
        y = tree_minimum(z.right)
        if parent(T, y) is not z:
            transplant(T, y, y.right)
            y.right = z.right
            y.right.succ = z.right.succ
        transplant(T, z, y)
        y.left = z.left
        y.left.succ = z.left.succ


def transplant(T, u, v):
    if not parent(T, u):
        T.root = v
    elif u == parent(T, u).left:
        parent(T, u).left = v
    else:
        parent(T, u).right = v
    if v:
        parent(T, v) = parent(T, u)


def parent(T, z):
    if z == T.root:
        return None
    cur = T.root
    while cur != z:
        p = cur
        cur = cur.left if cur.key > z.key else cur.right
    return p


def tree_minimum(root):
    if root is None:
        return None
    if root.left is None:
        return root
    return tree_minimum(root.left)


def tree_maximum(root):
    if root is None:
        return None
    if root.right is None:
        return root
    return tree_maximum(root.right)


if __name__ == '__main__':
    unittest.main()
