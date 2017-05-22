import random
import unittest
from .heap_util import random_max_heap, check_max_heap


def parent(i):
    return (i - 1) // 2


def left(i):
    return 2*i + 1


def right(i):
    return 2*i + 2


def max_heapify_loop(A, i):
    heap_size = len(A)
    while True:
        l, r = left(i), right(i)
        largest = i
        if l < heap_size and A[l] > A[largest]:
            largest = l
        if r < heap_size and A[r] > A[largest]:
            largest = r
        if largest == i:
            break
        A[i], A[largest] = A[largest], A[i]
        i = largest


class MaxHeapifyTestCase(unittest.TestCase):

    def test_random(self):
        for _ in range(10000):
            heap = random_max_heap()
            idx = random.randint(0, len(heap)-1)
            if idx == 0:
                heap[0] = random.randint(1, 100)
            else:
                heap[idx] = heap[parent(idx)] - random.randint(0, 10)
            max_heapify_loop(heap, idx)
            self.assertTrue(check_max_heap(heap))


if __name__ == '__main__':
    unittest.main()