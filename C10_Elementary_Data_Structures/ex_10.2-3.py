import random
import unittest


class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = None


class Queue:
    def __init__(self):
        self.L = SinglyLinkedList()

    def enqueue(self, k):
        x = Node(k)
        if self.L.tail is None:
            self.L.tail = x
            self.L.head.next = x
            return
        self.L.tail.next = x
        self.L.tail = x

    def dequeue(self):
        if self.L.head.next is None:
            return None
        x = self.L.head.next.key
        self.L.head = self.L.head.next
        return x


class ProblemTestCase(unittest.TestCase):
    def test_random(self):
        for _ in range(100):
            q = Queue()
            queue = []
            for _ in range(10000):
                op = random.randint(1, 2)
                if op == 1:
                    x = q.dequeue()
                    if len(queue) == 0:
                        y = None
                    else:
                        y = queue[0]
                        del queue[0]
                    self.assertEqual(x, y)
                else:
                    x = random.randint(0, 100)
                    q.enqueue(x)
                    queue.append(x)


if __name__ == '__main__':
    unittest.main()
