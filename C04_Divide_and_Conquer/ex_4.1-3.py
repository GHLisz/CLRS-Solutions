# The question is specific to the implementation and the computer, so I will skip it.
# Though it's almost certain that the mixed method will change the crossover point.


import math
import random
import unittest

CROSSOVER_POINT = 20


def find_maximum_subarray_mixed(A, low, high):
    if high - low < CROSSOVER_POINT:
        return find_maximum_subarray_brute_force(A[low:high + 1])

    mid = (low + high) // 2
    left_low, left_high, left_sum = find_maximum_subarray(A, low, mid)
    right_low, right_high, right_sum = find_maximum_subarray(A, mid + 1, high)
    cross_low, cross_high, cross_sum = find_max_crossing_subarray(A, low, mid, high)

    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_low, left_high, left_sum
    if right_sum >= left_sum and right_sum >= cross_sum:
        return right_low, right_high, right_sum
    return cross_low, cross_high, cross_sum


def find_max_crossing_subarray(A, low, mid, high):
    left_sum = -math.inf
    sum = 0
    for i in range(mid, low - 1, -1):
        sum = sum + A[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i

    right_sum = -math.inf
    sum = 0
    for j in range(mid + 1, high + 1):
        sum = sum + A[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j

    return max_left, max_right, left_sum + right_sum


def find_maximum_subarray(A, low, high):
    if low == high:
        return low, high, A[low]

    mid = (low + high) // 2
    left_low, left_high, left_sum = find_maximum_subarray(A, low, mid)
    right_low, right_high, right_sum = find_maximum_subarray(A, mid + 1, high)
    cross_low, cross_high, cross_sum = find_max_crossing_subarray(A, low, mid, high)

    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_low, left_high, left_sum
    if right_sum >= left_sum and right_sum >= cross_sum:
        return right_low, right_high, right_sum
    return cross_low, cross_high, cross_sum


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

    def test_brute_force_all_negative(self):
        self.assertEqual(self.find_maximum_subarray_brute_force([-2, -1, -3, -4]), (1, 1, -1))

    def test_brute_force_cross(self):
        self.assertEqual(self.find_maximum_subarray_brute_force([3, -1, 6, -4]), (0, 2, 8))

    def random_array(self):
        return [random.randint(-100, 100) for _ in range(random.randint(1, 100))]

    def test_all_negative(self):
        self.assertEqual(find_maximum_subarray_mixed([-2, -1, -3, -4], 0, 3), (1, 1, -1))

    def test_cross(self):
        self.assertEqual(find_maximum_subarray_mixed([3, -1, 6, -4], 0, 3), (0, 2, 8))

    def test_random(self):
        for _ in range(10000):
            arr = self.random_array()
            _, _, sub1 = find_maximum_subarray_mixed(arr, 0, len(arr) - 1)
            _, _, sub2 = self.find_maximum_subarray_brute_force(arr)
            self.assertEqual(sub1, sub2)
