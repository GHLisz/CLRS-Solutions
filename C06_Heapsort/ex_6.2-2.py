import random
import unittest
from .heap_util import random_min_heap, check_min_heap


def parent(i):
    return (i - 1) // 2


def left(i):
    return 2*i + 1


def right(i):
    return 2*i + 2


def min_heapify(A, i):
    heap_size = len(A)
    l, r = left(i), right(i)
    smallest = i
    if l < heap_size and A[l] < A[smallest]:
        smallest = l
    if r < heap_size and A[r] < A[smallest]:
        smallest = r
    if smallest != i:
        A[i], A[smallest] = A[smallest], A[i]
        min_heapify(A, smallest)


class MinHeapifyTestCase(unittest.TestCase):
    def test_random(self):
        for _ in range(10000):
            heap = random_min_heap()
            idx = random.randint(0, len(heap)-1)
            if idx == 0:
                heap[0] = random.randint(1, 100)
            else:
                heap[idx] = heap[parent(idx)] + random.randint(0, 10)
            min_heapify(heap, idx)
            self.assertTrue(check_min_heap(heap))


if __name__ == '__main__':
    unittest.main()
