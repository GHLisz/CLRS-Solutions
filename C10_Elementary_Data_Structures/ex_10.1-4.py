import random
import unittest


class Queue:
    def __init__(self, size):
        self.length = size
        self.Q = [0 for _ in range(self.length)]
        self.head = 0
        self.tail = 0

    def enqueue(self, x):
        if (self.tail + 1) % self.length == self.head:
            raise Exception('overflow')
        self.Q[self.tail] = x
        self.tail += 1
        if self.tail == self.length:
            self.tail = 0

    def dequeue(self):
        if self.head == self.tail:
            raise Exception('underflow')
        x = self.Q[self.head]
        self.head += 1
        if self.head == self.length:
            self.head = 0
        return x


class ProblemTestCase(unittest.TestCase):

    def test_underflow(self):
        q = Queue(1)
        with self.assertRaises(Exception) as context:
            q.dequeue()
        self.assertTrue(context.exception.args[0], 'underflow')

    def test_overflow(self):
        q = Queue(10)
        for i in range(9):
            q.enqueue(0)
        with self.assertRaises(Exception) as context:
            q.enqueue(0)
        self.assertTrue(context.exception.args[0], 'overflow')


if __name__ == '__main__':
    unittest.main()
