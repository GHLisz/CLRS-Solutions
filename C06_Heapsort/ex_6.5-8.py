def parent(i):
    return (i - 1) // 2


def left(i):
    return 2*i + 1


def right(i):
    return 2*i + 2


def heap_increase_key(A, i, key):
    assert(key >= A[i])
    while i > 0 and key > A[parent(i)]:
        A[i] = A[parent(i)]
        i = parent(i)
    A[i] = key


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


def heap_delete(A, i):
    if i == len(A) - 1:
        del A[-1]
    else:
        A[i] = A[-1]
        del A[-1]
        max_heapify(A, i)
        heap_increase_key(A, i, A[i])
