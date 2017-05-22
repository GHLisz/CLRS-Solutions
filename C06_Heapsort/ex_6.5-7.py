import math
import random
import unittest


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


def heap_minimum(A):
    return A[0]


def heap_extract_min(A):
    assert len(A) > 0
    min_val = heap_minimum(A)
    A[0] = A[-1]
    del A[-1]
    min_heapify(A, 0)
    return min_val


def heap_decrease_key(A, i, key):
    assert key <= A[i]
    A[i] = key
    while i > 0 and A[parent(i)] > A[i]:
        A[i], A[parent(i)] = A[parent(i)], A[i]
        i = parent(i)


def min_heap_insert(A, key):
    A.append(math.inf)
    heap_decrease_key(A, len(A)-1, key)


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
    heap_increase_key(A, len(A)-1, key)


class Queue:
    def __init__(self):
        self.heap = []
        self.inc = 0

    def push(self, val):
        self.inc += 1
        min_heap_insert(self.heap, val)

    def front(self):
        return heap_minimum(self.heap)

    def pop(self):
        return heap_extract_min(self.heap)


class Stack:
    def __init__(self):
        self.heap = []
        self.inc = 0

    def push(self, val):
        self.inc += 1
        max_heap_insert(self.heap, val)

    def top(self):
        return heap_maximum(self.heap)

    def pop(self):
        return heap_extract_max(self.heap)


class QueueTestCase(unittest.TestCase):
    def test_random(self):
        a = []
        q = Queue()
        for _ in range(10000):
            op = random.randint(1, 5)
            if len(a) == 0:
                op = 3
            if op == 1:
                self.assertTrue(q.front(), a[0])
            elif op == 2:
                self.assertTrue(q.pop(), a[0])
                del a[0]
            else:
                val = random.randint(1, 100000)
                a.append(val)
                q.push(val)


class StackTestCase(unittest.TestCase):
    def test_random(self):
        a = []
        q = Stack()
        for _ in range(10000):
            op = random.randint(1, 5)
            if len(a) == 0:
                op = 3
            if op == 1:
                self.assertTrue(q.top(), a[-1])
            elif op == 2:
                self.assertTrue(q.pop(), a[-1])
                del a[-1]
            else:
                val = random.randint(1, 100000)
                a.append(val)
                q.push(val)


if __name__ == '__main__':
    unittest.main()
