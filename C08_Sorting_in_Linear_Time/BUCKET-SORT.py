import random
import unittest


def bucket_sort(A):
    n = len(A)
    buckets = [[] for _ in range(n)]
    for val in A:
        buckets[int(n * val)].append(val)
    out = []
    for b in buckets:
        insertion_sort(b)
        out += b
    return out


def insertion_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key


class SortTestCase(unittest.TestCase):
    @staticmethod
    def random_array():
        a = [random.randint(0, 99) for _ in range(random.randint(1, 100))]
        return [i/100 for i in a]

    def test_random(self):
        for _ in range(10000):
            arr = self.random_array()
            sorted_arr = sorted(arr)
            self.assertEqual(bucket_sort(arr), sorted_arr)

if __name__ == '__main__':
    unittest.main()
