import unittest


class Node:
    def __init__(self, key):
        self.key = key
        self.is_last_sibling = False   # indicate if the node is the last sibling
        self.left_child = None
        self.next = None  # if the node is last sibling, it points to parent, else it points to right sibling


def print_children(node):
    while True:
        print(node.key)
        node = node.next
        if node.is_last_sibling:
            break


def print_parent(node):
    while not node.is_last_sibling:
        node = node.next
    print(node.next.key)
