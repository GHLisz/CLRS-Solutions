import unittest


class DoublyLinkedList:
    def __init__(self, key):
        self.head = 0
        self.key_array = [key, ]
        self.next_array = [-1, ]
        self.prev_array = [-1, ]


def list_search(L, k):
    cur = L.head
    while L.next_array[cur] != -1 and L.key_array[cur] != k:
        cur = L.next_array[cur]
    if L.key_array[cur] == k:
        return cur
    else:
        return None


def list_insert(L, key):
    L.key_array.append(key)
    L.next_array.append(L.head)
    L.prev_array.append(-1)

    L.head = len(L.key_array) - 1
    L.prev_array[L.next_array[L.head]] = L.head


def list_delete(L, x):
    if L.prev_array[x] != -1:
        L.next_array[L.prev_array[x]] = L.next_array[x]
    else:
        L.head = L.next_array[x]
    if L.next_array[x] != -1:
        L.prev_array[L.next_array[x]] = L.prev_array[x]


class ProblemTestCase(unittest.TestCase):
    @staticmethod
    def list_to_str(L):
        print(L.head)
        print(L.next_array)
        print(L.key_array)
        print(L.prev_array)
        keys = []
        cur = L.head
        while True:
            keys.append(L.key_array[cur])
            if L.next_array[cur] == -1:
                break
            cur = L.next_array[cur]
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
        list_delete(L, 2)
        self.assertEqual(self.list_to_str(L), '5 4 2 1')

if __name__ == '__main__':
    unittest.main()
