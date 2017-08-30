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


def left_rotate(T, x):
    y = x.right

    x.right = y.left
    if y.left:
        y.left.p = x

    y.p = x.p
    if not x.p:
        T.root = y
    elif x == x.p.left:
        x.p.left = y
    else:
        x.p.right = y

    y.left = x
    x.p = y


def right_rotate(T, y):
    x = y.left

    y.left = x.right
    if x.right:
        x.right.p = y

    x.p = y.p
    if not y.p:
        T.root = x
    elif y == y.p.left:
        y.p.left = x
    else:
        y.p.right = x

    x.right = y
    y.p = x
