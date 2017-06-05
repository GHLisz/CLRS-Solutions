import random
import unittest


class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


class SinglyLinkedList:
    def __init__(self, key):
        self.head = Node(key)


def insert(L, x):
    x.next = L.head
    L.head = x


def reverse(L):
    new_head = L.head
    cur = L.head.next
    new_head.next = None

    while cur is not None:
        nxt = cur.next
        cur.next = new_head
        new_head = cur
        cur = nxt
    L.head = new_head


class ProblemTestCase(unittest.TestCase):
    @staticmethod
    def list_to_str(node):
        keys = []
        cur = node
        while cur is not None:
            keys.append(cur.key)
            cur = cur.next
        return ' '.join(map(str, keys))

    def test_case(self):
        L = SinglyLinkedList(1)
        insert(L, Node(2))
        insert(L, Node(3))
        insert(L, Node(4))
        insert(L, Node(5))
        self.assertEqual(self.list_to_str(L.head), '5 4 3 2 1')
        reverse(L)
        self.assertEqual(self.list_to_str(L.head), '1 2 3 4 5')

if __name__ == '__main__':
    unittest.main()
