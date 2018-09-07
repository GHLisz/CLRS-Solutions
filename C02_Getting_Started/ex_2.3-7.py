import math
import random
import unittest


def two_sum(S, x):
    l, r = 0, len(S) - 1
    merge_sort(S, l, r)
    while l < r:
        if S[l] + S[r] < x:
            l += 1
        elif S[l] + S[r] > x:
            r -= 1
        else:
            return True
    return False


def merge(A, p, q, r):
    L = A[p:q + 1]
    R = A[q + 1:r + 1]
    L.append(math.inf)
    R.append(math.inf)
    i, j = 0, 0
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)


class InsertionSortTestCase(unittest.TestCase):
    def random_array(self):
        return [random.randint(0, 100) for _ in range(random.randint(1, 100))]

    def brute_force(self, a, x):
        for i in range(len(a)):
            for j in range(i + 1, len(a)):
                if a[i] + a[j] == x:
                    return True
        return False

    def test_merge_sort(self):
        for _ in range(10000):
            arr = self.random_array()
            sorted_arr = sorted(arr)
            merge_sort(arr, 0, len(arr) - 1)
            self.assertEqual(arr, sorted_arr)

    def test_two_sum(self):
        for _ in range(10000):
            a = sorted(self.random_array())
            x = random.randint(0, 200)
            self.assertEqual(two_sum(a, x), self.brute_force(a, x))


if __name__ == '__main__':
    unittest.main()
