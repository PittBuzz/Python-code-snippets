import unittest


def arraySubdivision(n, a, d, m):
    """

    This function will count the number of ways to select m
    consecutive elements summing to d in an list s of length n.
    E.g.
        a = [1, 2, 1, 3, 2]
        m = 2
        d = 3

        -> 2 ways: (1, 2) and (2, 1)

    """

    result = 0
    for i in range(n - m + 1):
        if sum(a[i:i + m]) == d:
            result += 1
    return result


class TestUM(unittest.TestCase):

    def setUp(self):
        pass

    def testArraySubDivision(self):
        self.assertEqual(arraySubdivision(5, [1, 2, 1, 3, 2], 3, 2), 2)
        self.assertEqual(arraySubdivision(5, [1, 1, 1, 1, 1], 3, 2), 0)
        self.assertEqual(arraySubdivision(1, [4], 4, 1), 1)


if __name__ == '__main__':
    unittest.main()
