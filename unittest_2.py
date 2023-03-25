import unittest
import random


def n_random_nums(n):
    nums = []
    for i in range(n):
        nums.append(random.random())
    return nums


class NumbersTest(unittest.TestCase):

    def test_half(self):
        for i in n_random_nums(10):
            with self.subTest(i=i):
                self.assertGreaterEqual(i, 0.5)


if __name__ == '__main__':
    unittest.main()
