import random
import unittest


def parent(i):
    return (i - 1) // 2


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def max_heapify(A, i, heap_size):
    l, r = left(i), right(i)
    largest = i
    if l < heap_size and A[l] > A[largest]:
        largest = l
    if r < heap_size and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest, heap_size)


def build_max_heap(A):
    heap_size = len(A)
    for i in range(parent(heap_size - 1), -1, -1):
        max_heapify(A, i, heap_size)


def heap_sort(A):
    build_max_heap(A)
    heap_size = len(A)
    for i in range(len(A) - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heap_size -= 1
        max_heapify(A, 0, heap_size)


class HeapSortTestCase(unittest.TestCase):
    def random_array(self):
        return [random.randint(0, 100) for _ in range(random.randint(1, 100))]

    def test_simple(self):
        arr = [30, 65, 51, 14, 28, 1, 40, 93, 65, 30, 92]
        sorted_arr = sorted(arr)
        heap_sort(arr)
        self.assertEqual(arr, sorted_arr)

    def test_random(self):
        for _ in range(10000):
            arr = self.random_array()
            sorted_arr = sorted(arr)
            heap_sort(arr)
            self.assertEqual(arr, sorted_arr)


if __name__ == '__main__':
    unittest.main()
