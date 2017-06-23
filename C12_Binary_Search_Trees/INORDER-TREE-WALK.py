import random
import unittest


class TreeNode:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


def inorder_tree_walk(x):
    if x is not None:
        inorder_tree_walk(x.left)
        print(x.key)
        inorder_tree_walk(x.right)


class ProblemTestCase(unittest.TestCase):
    def test_case(self):
        root = TreeNode(3,
                        TreeNode(1, TreeNode(0), TreeNode(2)),
                        TreeNode(5, TreeNode(4), TreeNode(6)))
        inorder_tree_walk(root)


if __name__ == '__main__':
    unittest.main()
