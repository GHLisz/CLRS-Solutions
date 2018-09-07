import random
import unittest

m = 5


class LinearProbing:
    def __init__(self):
        global m
        self.slots = [None for _ in range(m)]

    def hash_insert(self, key):
        global m
        i = 0
        while True:
            pos = (key + i) % m
            if self.slots[pos] is None or self.slots[pos] == '[Deleted]':
                break
            i += 1
        self.slots[pos] = key

    def hash_delete(self, key):
        global m
        i = 0
        while True:
            pos = (key + i) % m
            if self.slots[pos] is None:
                break
            if self.slots[pos] == key:
                self.slots[pos] = '[Deleted]'
                break
            i += 1


class ProblemTestCase(unittest.TestCase):

    def test_case(self):
        l = LinearProbing()
        l.hash_insert(0)
        l.hash_insert(5)
        l.hash_insert(10)
        self.assertEqual(l.slots, [0, 5, 10, None, None])
        l.hash_delete(5)
        self.assertEqual(l.slots, [0, '[Deleted]', 10, None, None])
        l.hash_delete(10)
        self.assertEqual(l.slots, [0, '[Deleted]', '[Deleted]', None, None])
        l.hash_insert(15)
        self.assertEqual(l.slots, [0, 15, '[Deleted]', None, None])


if __name__ == '__main__':
    unittest.main()
