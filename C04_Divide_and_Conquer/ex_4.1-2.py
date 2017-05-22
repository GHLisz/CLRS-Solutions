import math
import unittest


def find_maximum_subarray_brute_force(A):
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


class FindMaximumSubarryTestCase(unittest.TestCase):
    def test_brute_force_all_negative(self):
        self.assertEqual(find_maximum_subarray_brute_force([-2, -1, -3, -4]), (1, 1, -1))

    def test_brute_force_cross(self):
        self.assertEqual(find_maximum_subarray_brute_force([3, -1, 6, -4]), (0, 2, 8))
