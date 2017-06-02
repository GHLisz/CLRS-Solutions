import random
import unittest


class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


class SinglyLinkedList:
    def __init__(self, key):
        self.head = Node(key)


class Stack:
    def __init__(self):
        self.L = SinglyLinkedList(None)

    def stack_empty(self):
        return self.L.head.next is None

    def push(self, k):
        x = Node(k)
        x.next = self.L.head
        self.L.head = x

    def pop(self):
        if self.stack_empty():
            raise Exception('underflow')
        x = self.L.head
        self.L.head = self.L.head.next
        return x.key


class ProblemTestCase(unittest.TestCase):
    def test_underflow(self):
        s = Stack()
        with self.assertRaises(Exception) as context:
            s.pop()
        self.assertTrue(context.exception.args[0], 'underflow')

    def test_random(self):
        s = Stack()
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
