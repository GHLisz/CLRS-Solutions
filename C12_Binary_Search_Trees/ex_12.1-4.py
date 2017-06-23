import random
import unittest


class TreeNode:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


def preorder_tree_walk(x):
    if x is not None:
        print(x.key)
        preorder_tree_walk(x.left)
        preorder_tree_walk(x.right)


def postorder_tree_walk(x):
    if x is not None:
        postorder_tree_walk(x.left)
        postorder_tree_walk(x.right)
        print(x.key)


class ProblemTestCase(unittest.TestCase):
    def test_case(self):
        root = TreeNode(3,
                        TreeNode(1, TreeNode(0), TreeNode(2)),
                        TreeNode(5, TreeNode(4), TreeNode(6)))
        preorder_tree_walk(root)
        postorder_tree_walk(root)


if __name__ == '__main__':
    unittest.main()
