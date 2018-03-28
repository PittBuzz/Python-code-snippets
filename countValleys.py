import unittest


def countValleys(n, s):
    """

    Given a set of steps, either up or down.
    Count the number of mountains (start at 0, goes up, returns to 0)
    and the number of valleys (start at 0, goes down, returns to 0).

    Input:
        n -- number of steps
        s -- string describing the steps ('U' or 'D')

    """
    height = [0]
    for i in range(n):
        if s[i] == 'U':
            height.append(height[-1] + 1)
        elif s[i] == 'D':
            height.append(height[-1] - 1)

    zeros = [i for i, x in enumerate(height) if x == 0]
    valleys = 0
    mountains = 0

    for i in zeros:
        if i != 0:
            if height[i - 1] > 0:
                mountains += 1
            elif height[i - 1] < 0:
                valleys += 1

    return valleys


class TestUM(unittest.TestCase):

    def setUp(self):
        pass

    def testCountValleys(self):
        self.assertEqual(countValleys(8, 'UDDDUDUU'), 1)


if __name__ == '__main__':
    unittest.main()
