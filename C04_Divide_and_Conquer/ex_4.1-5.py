import math
import random
import unittest


def find_maximum_subarray_linear(A):
    max_ending_here = max_so_far = A[0]
    max_ending_here_start, start, end = 0, 0, 0

    for i in range(1, len(A)):
        if A[i] >= max_ending_here + A[i]:  # consider the possibility of max_ending_here being another value
            max_ending_here = A[i]
            max_ending_here_start = i
        else:
            max_ending_here = max_ending_here + A[i]

        if max_so_far <= max_ending_here:
            max_so_far = max_ending_here
            start = max_ending_here_start
            end = i
    return start, end, max_so_far


class FindMaximumSubarryTestCase(unittest.TestCase):
    def find_maximum_subarray_brute_force(self, A):
        max_sum = -math.inf
        for i in range(len(A)):
            temp_sum = 0
            for j in range(i, len(A)):
                temp_sum += A[j]
                if max_sum < temp_sum:
                    max_sum = temp_sum
                    left_index = i
                    right_index = j
        return left_index, right_index, max_sum

    def random_array(self):
        return [random.randint(-100, 100) for _ in range(random.randint(1, 100))]

    def test_all_negative(self):
        self.assertEqual(find_maximum_subarray_linear([-2, -1, -3, -4]), (1, 1, -1))

    def test_cross(self):
        self.assertEqual(find_maximum_subarray_linear([3, -1, 6, -4]), (0, 2, 8))

    def test_random(self):
        for _ in range(10000):
            arr = self.random_array()
            _, _, sub1 = find_maximum_subarray_linear(arr)
            _, _, sub2 = self.find_maximum_subarray_brute_force(arr)
            self.assertEqual(sub1, sub2)
