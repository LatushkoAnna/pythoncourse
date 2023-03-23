import unittest


def same_type(a, b):
    if type(a) == type(b):
        return True
    else:
        return False


def dividers(a):
    divs = []
    for i in range(a):
        if a % (i + 1) == 0:
            divs.append(i + 1)
    return divs


def exp(a, b):
    return a ** b


def squares(a):
    sq = []
    i = 1
    while i ** 2 <= a:
        sq.append(i ** 2)
        i += 1
    return sq


class TestTest(unittest.TestCase):

    def test_same_type_true(self):
        self.assertTrue(same_type(-28192.124, 25j))

    def test_same_type_false(self):
        self.assertFalse(same_type(12e2, -1.0))

    def test_dividers_in(self):
        self.assertIn(7100, dividers(127818))

    def test_dividers_notin(self):
        self.assertNotIn(7101, dividers(127818))

    def test_exp_greater(self):
        self.assertGreater(exp(4, 3), exp(3, 4))

    def test_exp_less(self):
        self.assertLess(exp(3, 4), exp(4, 3))

    def test_squares(self):
        self.assertCountEqual(squares(168), squares(170))


if __name__ == '__main__':
    unittest.main()
