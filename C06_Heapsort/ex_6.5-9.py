import math


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


def merge_lists(lists):
    k = len(lists)
    heap = []
    for i in range(k):
        if len(lists[i]) > 0:
            min_heap_insert(heap, (lists[i][0], i))
    idx = [0 for lst in lists]
    a = []
    while len(heap) > 0:
        val, i = heap_extract_min(heap)
        a.append(val)
        idx[i] += 1
        if idx[i] < len(lists[i]):
            min_heap_insert(heap, (lists[i][idx[i]], i))
    return a