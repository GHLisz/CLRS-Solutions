import random
import unittest


def randomized_select_iterative(A, p, r, i):
    while True:
        if p == r:
            return A[p]
        q = randomized_partition(A, p, r)
        k = q - p + 1
        if i == k:
            return A[q]
        elif i < k:
            r = q - 1
        else:
            p = q + 1
            i -= k


def randomized_partition(A, p, r):
    i = random.randint(p, r)
    A[r], A[i] = A[i], A[r]
    return partition(A, p, r)


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1


class SelectTestCase(unittest.TestCase):
    def test_random(self):
        for _ in range(1000):
            a = [random.randint(1, 1000000) for _ in range(random.randint(1, 1000))]
            i = random.randint(1, len(a))
            b = sorted(a)
            self.assertTrue(randomized_select_iterative(a, 0, len(a)-1, i), b[i-1])


if __name__ == '__main__':
    unittest.main()
