import unittest


class DoublyLinkedList:
    def __init__(self):
        self.head = -1
        self.free = 0
        self.key_array = [0 for _ in range(10)]
        self.next_array = [i + 1 for i in range(10)]
        self.next_array[-1] = -1
        self.prev_array = [0 for _ in range(10)]


def compactify_list(L):
    if L.free == -1:
        return

    cur = L.free
    while cur != -1:
        L.prev_array[cur] = -2
        cur = L.next_array[cur]

    left, right = 0, len(L.key_array) - 1
    while True:
        while L.prev_array[left] != -2:
            left += 1
        while L.prev_array[right] == -2:
            right -= 1

        if left >= right:
            break

        if right == L.head:
            L.head = left

        L.prev_array[left] = L.prev_array[right]
        L.next_array[left] = L.next_array[right]
        L.key_array[left] = L.key_array[right]

        L.next_array[right] = left  # record pos after the exchange

        left += 1
        right -= 1
    right += 1

    for x in range(0, right):
        if L.prev_array[x] >= right:
            L.prev_array[x] = L.next_array[L.prev_array[x]]
        if L.next_array[x] >= right:
            L.next_array[x] = L.next_array[L.next_array[x]]

    for x in range(right, len(L.key_array) - 1):
        L.next_array[x] = x + 1
    L.next_array[x] = -1

    L.free = right


def allocate_object(L):
    if L.free == -1:
        raise Exception('out of space')
    x = L.free
    L.free = L.next_array[x]
    return x


def free_object(L, x):
    L.next_array[x] = L.free
    L.free = x


def list_search(L, k):
    cur = L.head
    while L.next_array[cur] != -1 and L.key_array[cur] != k:
        cur = L.next_array[cur]
    if L.key_array[cur] == k:
        return cur
    else:
        return None


def list_insert(L, key):
    x = allocate_object(L)
    L.key_array[x] = key
    L.next_array[x] = L.head
    L.prev_array[x] = -1

    if L.head != -1:
        L.prev_array[L.head] = x
    L.head = x


def list_delete(L, x):
    if L.prev_array[x] != -1:
        L.next_array[L.prev_array[x]] = L.next_array[x]
    else:
        L.head = L.next_array[x]
    if L.next_array[x] != -1:
        L.prev_array[L.next_array[x]] = L.prev_array[x]
    free_object(L, x)


class ProblemTestCase(unittest.TestCase):
    @staticmethod
    def list_to_str(L):
        print(L.head)
        print(L.free)
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
        L = DoublyLinkedList()
        list_insert(L, 1)
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
        compactify_list(L)
        self.assertEqual(self.list_to_str(L), '5 4 2 1')
        x = list_search(L, 2)
        list_delete(L, x)
        compactify_list(L)
        self.assertEqual(self.list_to_str(L), '5 4 1')


if __name__ == '__main__':
    unittest.main()
