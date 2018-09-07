import random
import unittest


def binary_search(A, v):
    low, high = 0, len(A) - 1
    while low <= high:
        mid = (low + high) // 2
        if A[mid] < v:
            low = mid + 1  # think about the extra 1
        elif A[mid] > v:
            high = mid - 1
        else:
            return mid
    return None


class BinarySearchTestCase(unittest.TestCase):
    def random_array(self):
        return [random.randint(0, 100) for _ in range(random.randint(1, 100))]

    def test_random(self):
        for _ in range(10000):
            sorted_arr = sorted(self.random_array())
            val = random.randint(0, 110)
            if val in sorted_arr:
                val_index = binary_search(sorted_arr, val)
                self.assertEqual(val, sorted_arr[val_index])
            else:
                self.assertIsNone(binary_search(sorted_arr, val))


if __name__ == '__main__':
    unittest.main()
