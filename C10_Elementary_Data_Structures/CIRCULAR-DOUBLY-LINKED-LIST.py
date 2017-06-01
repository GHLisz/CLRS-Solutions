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


def list_search(L, k):
    x = L.nil.next
    while x is not L.nil and x.key != k:
        x = x.next
    return x


def list_insert(L, x):
    x.next = L.nil.next
    L.nil.next.prev = x
    L.nil.next = x
    x.prev = L.nil


def list_delete(L, x):
    x.prev.next = x.next
    x.next.prev = x.prev


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
        L = CircularDoublyLinkedList()
        list_insert(L, Node(1))
        self.assertEqual(self.list_to_str(L.nil.next), '1')
        list_insert(L, Node(2))
        list_insert(L, Node(3))
        list_insert(L, Node(4))
        list_insert(L, Node(5))
        self.assertEqual(self.list_to_str(L.nil.next), '5 4 3 2 1')
        node_to_del = list_search(L, 3)
        self.assertEqual(self.list_to_str(node_to_del), '3 2 1')
        list_delete(L, node_to_del)
        self.assertEqual(self.list_to_str(L.nil.next), '5 4 2 1')

if __name__ == '__main__':
    unittest.main()
