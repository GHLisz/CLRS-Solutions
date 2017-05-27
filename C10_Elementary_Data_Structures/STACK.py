import random
import unittest


class Stack:
    def __init__(self, size):
        self.S = [0 for _ in range(size)]
        self.top = -1

    def stack_empty(self):
        return self.top == -1

    def push(self, x):
        self.top += 1
        self.S[self.top] = x

    def pop(self):
        if self.stack_empty():
            raise Exception('underflow')
        else:
            self.top -= 1
            return self.S[self.top + 1]


class ProblemTestCase(unittest.TestCase):
    def test_underflow(self):
        s = Stack(5)
        with self.assertRaises(Exception) as context:
            s.pop()
        self.assertTrue(context.exception.args[0], 'underflow')

    def test_random(self):
        s = Stack(100001)
        test_s = []
        for _ in range(10000):
            op = random.randint(1, 3)
            if op >= 2:
                x = random.randint(1, 100000)
                s.push(x)
                test_s.append(x)
            else:
                if len(test_s) == 0:
                    with self.assertRaises(Exception) as context:
                        s.pop()
                    self.assertTrue(context.exception.args[0], 'underflow')
                else:
                    x = s.pop()
                    y = test_s[-1]
                    del test_s[-1]
                    self.assertEqual(x, y)


if __name__ == '__main__':
    unittest.main()
