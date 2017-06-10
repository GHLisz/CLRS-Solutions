import unittest


class DoublyLinkedList:
    def __init__(self, key):
        self.head = 0
        self.arr = [key, -1, -1]  # key, next, prev


def list_search(L, k):
    cur = L.head
    while L.arr[cur+1] != -1 and L.arr[cur] != k:
        cur = L.arr[cur+1]
    if L.arr[cur] == k:
        return cur
    else:
        return None


def list_insert(L, key):
    L.arr.extend([key, L.head, -1])

    L.head = len(L.arr) - 3
    L.arr[L.arr[L.head+1]+2] = L.head


def list_delete(L, x):   # x is a pointer
    if L.arr[x+2] != -1:
        L.arr[L.arr[x+2]+1] = L.arr[x+1]
    else:
        L.head = L.arr[x+1]
    if L.arr[x+1] != -1:
        L.arr[L.arr[x+1]+2] = L.arr[x+2]


class ProblemTestCase(unittest.TestCase):
    @staticmethod
    def list_to_str(L):
        print(L.head)
        print(L.arr)
        keys = []
        cur = L.head
        while True:
            keys.append(L.arr[cur])
            if L.arr[cur+1] == -1:
                break
            cur = L.arr[cur+1]
        return ' '.join(map(str, keys))

    def test_case(self):
        L = DoublyLinkedList(1)
        self.assertEqual(self.list_to_str(L), '1')
        list_insert(L, 2)
        self.assertEqual(self.list_to_str(L), '2 1')
        list_insert(L, 3)
        self.assertEqual(self.list_to_str(L), '3 2 1')
        list_insert(L, 4)
        self.assertEqual(self.list_to_str(L), '4 3 2 1')
        list_insert(L, 5)
        self.assertEqual(self.list_to_str(L), '5 4 3 2 1')
        list_delete(L, 6)
        self.assertEqual(self.list_to_str(L), '5 4 2 1')

if __name__ == '__main__':
    unittest.main()
