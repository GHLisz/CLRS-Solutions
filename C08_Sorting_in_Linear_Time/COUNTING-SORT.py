import random
import unittest


def counting_sort(A, k):
    B = [0 for _ in range(len(A))]
    C = [0 for _ in range(k+1)]
    for num in A:
        C[num] = C[num] + 1
    # C[i] now contains the number of elements equal to i.
    for i in range(k):
        C[i+1] = C[i+1] + C[i]
    # C[i] now contains the number of elements less than or equal to i.
    for num in A:  # reversed(A):
        B[C[num]-1] = num  # !!! -1
        C[num] -= 1
    return B


class SortTestCase(unittest.TestCase):
    @staticmethod
    def random_array():
        return [random.randint(0, 100) for _ in range(random.randint(1, 100))]

    def test_random(self):
        for _ in range(10000):
            arr = self.random_array()
            sorted_arr = sorted(arr)
            b = counting_sort(arr, 100)
            self.assertEqual(b, sorted_arr)

if __name__ == '__main__':
    unittest.main()
