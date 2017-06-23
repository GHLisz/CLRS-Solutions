import random
import unittest


class TreeNode:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


def inorder_tree_walk_nonrecursive(x):
    stack = []
    while len(stack) > 0 or x is not None:
        if x is None:
            x = stack.pop()
            print(x.key)
            x = x.right
        else:
            stack.append(x)
            x = x.left


class ProblemTestCase(unittest.TestCase):
    def test_case(self):
        root = TreeNode(3,
                        TreeNode(1, TreeNode(0), TreeNode(2)),
                        TreeNode(5, TreeNode(4), TreeNode(6)))
        inorder_tree_walk_nonrecursive(root)


if __name__ == '__main__':
    unittest.main()
