import random
import unittest


class CountInterval:
    def __init__(self, A):
        k = max(A)
        self.C = [0 for _ in range(k + 1)]
        for num in A:
            self.C[num] += 1
        for i in range(k):
            self.C[i + 1] += self.C[i]

    def count(self, a, b):
        if a == 0:
            return self.C[b]
        return self.C[b] - self.C[a - 1]


class CountIntervalTestCase(unittest.TestCase):
    def test_random(self):
        for _ in range(1000):
            arr = [random.randint(0, 1000) for _ in range(random.randint(1, 1000))]
            c = CountInterval(arr)
            k = max(arr)
            for _ in range(100):
                a = random.randint(0, k)
                b = random.randint(0, k)
                if a > b:
                    continue
                num = c.count(a, b)
                self.assertEqual(num, len(list(filter(lambda x: a <= x <= b, arr))))


if __name__ == '__main__':
    unittest.main()
