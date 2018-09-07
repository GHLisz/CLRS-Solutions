import random
import unittest


def merge(A, p, q, r):
    L = A[p:q + 1]  # items start through end-1, excluding end
    R = A[q + 1:r + 1]
    i, j, k = 0, 0, p
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
    # if all L's elements are copied back, then the remaining elements of A are already the highest ones.
    if j == len(R):
        A[k:r + 1] = L[i:]


def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)


class InsertionSortTestCase(unittest.TestCase):
    def random_array(self):
        return [random.randint(0, 100) for _ in range(random.randint(1, 100))]

    def test_random(self):
        for _ in range(10000):
            arr = self.random_array()
            sorted_arr = sorted(arr)
            merge_sort(arr, 0, len(arr) - 1)
            self.assertEqual(arr, sorted_arr)


if __name__ == '__main__':
    unittest.main()
