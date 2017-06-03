import random
import unittest


class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
        self.prev = None


class CircularDoublyLinkedList:
    def __init__(self):
        self.nil = Node(None)
        self.nil.next = self.nil
        self.nil.prev = self.nil

    def values(self):
        values = []
        cur = self.nil.next
        while cur is not self.nil:
            values.append(cur.key)
            cur = cur.next
        return values


def list_insert(L, x):
    x.next = L.nil.next
    L.nil.next.prev = x
    L.nil.next = x
    x.prev = L.nil


def union(S1, S2):
    S1.nil.prev.next = S2.nil.next
    S2.nil.prev.next = S1.nil
    S2.nil.prev = None
    S2.nil.next = None
    return S1


class ProblemTestCase(unittest.TestCase):
    def test_case(self):
        list_1 = CircularDoublyLinkedList()
        list_insert(list_1, Node(1))
        list_insert(list_1, Node(3))
        list_insert(list_1, Node(5))
        list_2 = CircularDoublyLinkedList()
        list_insert(list_2, Node(2))
        list_insert(list_2, Node(4))
        list_insert(list_2, Node(6))
        union_list = union(list_1, list_2)
        self.assertTrue(sorted(union_list.values()), [1, 2, 3, 4, 5, 6])


if __name__ == '__main__':
    unittest.main()
