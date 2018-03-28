import unittest


def pageTurning(n, p):
    """

    Function to calculate how many pages one needs to turn in a book with n pages to get at page p.
    One can start at the front and at the back.

    """

    front = int(p / 2)
    if n % 2 == 0:
        # even
        back = int((n - p + 1) / 2)
    else:
        # uneven
        back = int((n - p) / 2)

    return min(front, back)


class TestUM(unittest.TestCase):

    def setUp(self):
        pass

    def test...(self):
        self.assertEqual(pageTurning(6, 2), 1)
        self.assertEqual(pageTurning(5, 4), 0)


if __name__ == '__main__':
    unittest.main()
