import random
import unittest


def radix_sort(A):
    d = len(str(max(A)))
    buckets = [[] for _ in range(10)]
    for i in range(1, d+1):
        for val in A:
            buckets[val % (10**i) // 10**(i-1)].append(val)
        del A[:]
        for b in buckets:
            A.extend(b)
        buckets = [[] for _ in range(10)]


class SortTestCase(unittest.TestCase):
    @staticmethod
    def random_array():
        return [random.randint(0, 100) for _ in range(random.randint(1, 100))]

    def test_random(self):
        for _ in range(10000):
            arr = self.random_array()
            sorted_arr = sorted(arr)
            radix_sort(arr)
            self.assertEqual(arr, sorted_arr)

if __name__ == '__main__':
    unittest.main()
