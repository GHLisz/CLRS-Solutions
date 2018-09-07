import random
import unittest

m = 11


def aux_hash(k):
    return k


def aux_hash2(k):
    return 1 + (k % (m - 1))


class OpenAddressing:
    def __init__(self):
        global m
        self.slots = [None for _ in range(m)]

    def h(self, k, i):
        raise NotImplementedError

    def hash_insert(self, key):
        global m
        i = 0
        while True:
            pos = self.h(key, i)
            if self.slots[pos] is None:
                break
            i += 1
        self.slots[pos] = key


class LinearProbing(OpenAddressing):
    def __init__(self):
        OpenAddressing.__init__(self)

    def h(self, k, i):
        return (aux_hash(k) + i) % m


class QuadraticProbing(OpenAddressing):
    def __init__(self):
        OpenAddressing.__init__(self)

    def h(self, k, i):
        return (aux_hash(k) + i + 3 * i * i) % m


class DoubleHashing(OpenAddressing):
    def __init__(self):
        OpenAddressing.__init__(self)

    def h(self, k, i):
        return (aux_hash(k) + i * aux_hash2(k)) % m


class ProblemTestCase(unittest.TestCase):

    def test_case(self):
        a = [10, 22, 31, 4, 15, 28, 17, 88, 59]
        l = LinearProbing()
        q = QuadraticProbing()
        d = DoubleHashing()
        for v in a:
            l.hash_insert(v)
            q.hash_insert(v)
            d.hash_insert(v)
        self.assertEqual(l.slots, [22, 88, None, None, 4, 15, 28, 17, 59, 31, 10])
        self.assertEqual(q.slots, [22, None, 88, 17, 4, None, 28, 59, 15, 31, 10])
        self.assertEqual(d.slots, [22, None, 59, 17, 4, 15, 28, 88, None, 31, 10])


if __name__ == '__main__':
    unittest.main()
