# INSERT O(1), DELETE O(n)
import unittest


class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


class SinglyLinkedList:
    def __init__(self, key):
        self.head = Node(key)


def list_search(L, k):
    x = L.head
    while x is not None and x.key != k:
        x = x.next
    return x


def list_insert(L, x):
    x.next = L.head
    L.head = x


def list_delete(L, x):
    if x is L.head:
        L.head = x.next
        return

    cur = L.head
    while cur is not x:
        x_prev = cur
        cur = cur.next
    x_prev.next = x.next


class ProblemTestCase(unittest.TestCase):
    @staticmethod
    def list_to_str(node):
        keys = []
        cur = node
        while cur:
            keys.append(cur.key)
            cur = cur.next
        return ' '.join(map(str, keys))

    def test_case(self):
        L = SinglyLinkedList(1)
        self.assertEqual(self.list_to_str(L.head), '1')
        list_insert(L, Node(2))
        list_insert(L, Node(3))
        list_insert(L, Node(4))
        list_insert(L, Node(5))
        self.assertEqual(self.list_to_str(L.head), '5 4 3 2 1')
        node_to_del = list_search(L, 3)
        self.assertEqual(self.list_to_str(node_to_del), '3 2 1')
        list_delete(L, node_to_del)
        self.assertEqual(self.list_to_str(L.head), '5 4 2 1')


if __name__ == '__main__':
    unittest.main()
