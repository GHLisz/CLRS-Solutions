import random
import unittest


class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


class CircularSinglyLinkedList:
    def __init__(self):
        self.nil = Node(None)
        self.nil.next = self.nil


def search(S, k):
    cur = S.nil.next
    while cur is not S.nil and cur.key != k:
        cur = cur.next
    if cur is S.nil:
        return None
    return cur


def insert(S, x):
    x.next = S.nil.next
    S.nil.next = x


def delete(S, x):
    prev = S.nil
    while prev.next is not x:
        prev = prev.next
    prev.next = prev.next.next
    x.next = None


class ProblemTestCase(unittest.TestCase):
    @staticmethod
    def list_to_str(node):
        keys = []
        cur = node
        while cur.key is not None:
            keys.append(cur.key)
            cur = cur.next
        return ' '.join(map(str, keys))

    def test_case(self):
        L = CircularSinglyLinkedList()
        insert(L, Node(1))
        self.assertEqual(self.list_to_str(L.nil.next), '1')
        insert(L, Node(2))
        insert(L, Node(3))
        insert(L, Node(4))
        insert(L, Node(5))
        self.assertEqual(self.list_to_str(L.nil.next), '5 4 3 2 1')
        node_to_del = search(L, 3)
        self.assertEqual(self.list_to_str(node_to_del), '3 2 1')
        delete(L, node_to_del)
        self.assertEqual(self.list_to_str(L.nil.next), '5 4 2 1')


if __name__ == '__main__':
    unittest.main()
