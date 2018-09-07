def parent(i):
    return (i - 1) // 2


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def heap_increase_key(A, i, key):
    assert (key >= A[i])
    while i > 0 and key > A[parent(i)]:
        A[i] = A[parent(i)]
        i = parent(i)
    A[i] = key
