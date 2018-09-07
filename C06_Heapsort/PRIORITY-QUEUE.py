import math
import random
import unittest
from heap_util import check_max_heap, random_max_heap


def parent(i):
    return (i - 1) // 2


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def max_heapify(A, i):
    heap_size = len(A)
    l, r = left(i), right(i)
    largest = i
    if l < heap_size and A[l] > A[largest]:
        largest = l
    if r < heap_size and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest)


def heap_maximum(A):
    return A[0]


def heap_extract_max(A):
    assert len(A) > 0
    max_val = heap_maximum(A)
    A[0] = A[-1]
    del A[-1]
    max_heapify(A, 0)
    return max_val


def heap_increase_key(A, i, key):
    assert key >= A[i]
    A[i] = key
    while i > 0 and A[parent(i)] < A[i]:
        A[i], A[parent(i)] = A[parent(i)], A[i]
        i = parent(i)


def max_heap_insert(A, key):
    A.append(-math.inf)
    heap_increase_key(A, len(A) - 1, key)


class PriorityQueueTestCase(unittest.TestCase):
    def test_heap_extract_max(self):
        for _ in range(1000):
            heap = random_max_heap()
            heap_size = len(heap)
            self.assertEqual(max(heap), heap_extract_max(heap))
            self.assertTrue(check_max_heap(heap))
            self.assertEqual(len(heap), heap_size - 1)

    def test_heap_increase_key(self):
        for _ in range(1000):
            heap = random_max_heap()
            heap_size = len(heap)
            i = random.randint(0, heap_size - 1)
            key = random.randint(200, 300)
            heap_increase_key(heap, i, key)
            self.assertTrue(check_max_heap(heap))

    def test_max_heap_insert(self):
        for _ in range(1000):
            heap = random_max_heap()
            heap_size = len(heap)
            key = random.randint(200, 300)
            max_heap_insert(heap, key)
            self.assertTrue(check_max_heap(heap))
            self.assertEqual(len(heap), heap_size + 1)


if __name__ == '__main__':
    unittest.main()
