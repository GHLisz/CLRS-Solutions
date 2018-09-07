import random
import unittest


def add_binary(a, b):
    n = len(a)
    c = [0 for _ in range(n + 1)]
    carry = 0
    for i in range(n):
        sum = a[i] + b[i] + carry
        if sum > 1:
            sum -= 2
            carry = 1
        else:
            carry = 0
        c[i] = sum
    c[n] = carry
    return c


class AddBinaryTestCase(unittest.TestCase):
    def bit_list_to_int(self, bit_list):
        bit_list.reverse()
        out = 0
        for bit in bit_list:
            out = (out << 1) | bit
        return out

    def test_bit_list_to_int(self):
        self.assertEqual(self.bit_list_to_int([0, 0, 0, 1]), 8)

    def random_bit_list(self, length):
        return [random.randint(0, 1) for _ in range(length)]

    def test_add_binary(self):
        for _ in range(10000):
            length = random.randint(1, 100)
            a, b = self.random_bit_list(length), self.random_bit_list(length)
            self.assertEqual(self.bit_list_to_int(add_binary(a, b)), self.bit_list_to_int(a) + self.bit_list_to_int(b))


if __name__ == '__main__':
    unittest.main()
