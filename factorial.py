import unittest


def factorial(n):
    """

    Computes the factorial in O(n)

    """

    result = 1
    while n > 0:
        result = result * n
        n -= 1

    return result


class TestUM(unittest.TestCase):

    def setUp(self):
        pass

    def testFactorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(6), 720)
        self.assertEqual(factorial(20), 2432902008176640000)


if __name__ == '__main__':
    unittest.main()
