import unittest


class DoublyLinkedList:
    def __init__(self):
        self.head = -1
        self.free = 0
        self.arr = [0 for _ in range(30)]  # key, next, prev
        for i in range(30):
            self.arr[i] = (i+2) if i % 3 == 1 else 0
        self.arr[-2] = -1


def allocate_object(L):
    if L.free == -1:
        raise Exception('out of space')
    x = L.free
    L.free = L.arr[x+1]
    return x


def free_object(L, x):
    L.arr[x+1] = L.free
    L.free = x


def list_search(L, k):
    cur = L.head
    while L.arr[cur+1] != -1 and L.arr[cur] != k:
        cur = L.arr[cur+1]
    if L.arr[cur] == k:
        return cur
    else:
        return None


def list_insert(L, key):
    x = allocate_object(L)
    L.arr[x] = key
    L.arr[x+1] = L.head
    L.arr[x+2] = -1

    if L.head != -1:
        L.arr[L.head+2] = x
    L.head = x


def list_delete(L, x):   # x is a pointer
    if L.arr[x+2] != -1:
        L.arr[L.arr[x+2]+1] = L.arr[x+1]
    else:
        L.head = L.arr[x+1]
    if L.arr[x+1] != -1:
        L.arr[L.arr[x+1]+2] = L.arr[x+2]
    free_object(L, x)


class ProblemTestCase(unittest.TestCase):
    @staticmethod
    def list_to_str(L):
        print(L.head)
        print(L.free)
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
        L = DoublyLinkedList()
        print(self.list_to_str(L))
        list_insert(L, 1)
        print(self.list_to_str(L))
        self.assertEqual(self.list_to_str(L), '1')
        list_insert(L, 2)
        self.assertEqual(self.list_to_str(L), '2 1')
        list_insert(L, 3)
        self.assertEqual(self.list_to_str(L), '3 2 1')
        list_insert(L, 4)
        self.assertEqual(self.list_to_str(L), '4 3 2 1')
        list_insert(L, 5)
        self.assertEqual(self.list_to_str(L), '5 4 3 2 1')
        x = list_search(L, 3)
        list_delete(L, x)
        self.assertEqual(self.list_to_str(L), '5 4 2 1')

if __name__ == '__main__':
    unittest.main()
