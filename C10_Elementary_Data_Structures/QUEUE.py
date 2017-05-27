import random
import unittest


class Queue:
    def __init__(self, size):
        self.length = size
        self.Q = [0 for _ in range(self.length)]
        self.head = 0
        self.tail = 0

    def enqueue(self, x):
        self.Q[self.tail] = x
        self.tail += 1
        if self.tail == self.length:
            self.tail = 0

    def dequeue(self):
        x = self.Q[self.head]
        self.head += 1
        if self.head == self.length:
            self.head = 0
        return x


class ProblemTestCase(unittest.TestCase):
    def test_this(self):
        q = Queue(100)
        test_q = []
        q.enqueue(5)
        test_q.append(5)
        q.enqueue(4)
        test_q.append(4)
        x = q.dequeue()
        y = test_q[0]
        del test_q[0]
        self.assertEqual(x, y)


if __name__ == '__main__':
    unittest.main()
