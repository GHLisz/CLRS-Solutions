'''
Outer loop invariant: at the start of each iteration, a[1..i-1] is the sorted smallest i-1 elements of the array
Inner loop invariant: at the start of each iteration, a[min_index] is the smallest number in the subarray a[i..j-1]
Why first n-1 elements? if there is a nth loop, it will compare a single element.
Best and worst running time are both Θ(n^2)
'''

import random
import unittest


def selection_sort(a):
    n = len(a)
    for i in range(0, n - 1):
        min_index = i
        for j in range(i + 1, n):
            if a[min_index] > a[j]:
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]


class InsertionSortTestCase(unittest.TestCase):
    def random_array(self):
        return [random.randint(0, 100) for _ in range(random.randint(1, 100))]

    def test_random(self):
        for _ in range(10000):
            arr = self.random_array()
            sorted_arr = sorted(arr)
            selection_sort(arr)
            self.assertEqual(arr, sorted_arr)


if __name__ == '__main__':
    unittest.main()
