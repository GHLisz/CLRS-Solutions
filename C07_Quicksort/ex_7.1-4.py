import random
import unittest


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] > x:
            i += 1
            A[j], A[i] = A[i], A[j]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1


def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q-1)
        quick_sort(A, q+1, r)


class SortTestCase(unittest.TestCase):
    @staticmethod
    def random_array():
        return [random.randint(0, 100) for _ in range(random.randint(1, 100))]

    def test_random(self):
        for _ in range(10000):
            arr = self.random_array()
            sorted_arr = sorted(arr)
            sorted_arr.reverse()
            quick_sort(arr, 0, len(arr)-1)
            self.assertEqual(arr, sorted_arr)


if __name__ == '__main__':
    unittest.main()
