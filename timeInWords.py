import unittest


def timeInWords(h, m):
    """

    Returns the time in words

    """

    d = {0: 'o\' clock', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
         6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
         11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
         15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
         19: 'nineteen', 20: 'twenty'}

    if m == 0:
        return str(d[h]) + ' o\' clock'
    elif m == 1:
        return 'one minute past ' + str(d[h])
    elif m == 15:
        return 'quarter past ' + str(d[h])
    elif m == 30:
        return 'half past ' + str(d[h])
    elif m == 45:
        return 'quarter to ' + str(d[h + 1])
    elif m <= 20:
        return d[m] + ' minutes past ' + str(h)
    elif m < 30:
        return d[m // 10 * 10] + ' ' + d[m % 10] + ' minutes past ' + str(d[h])
    elif m < 40:
        m = 60 - m
        return d[m // 10 * 10] + ' ' + d[m %
                                         10] + ' minutes to ' + str(d[h + 1])
    elif m < 60:
        m = 60 - m
        return d[m] + ' minutes to ' + str(d[h + 1])


class TestUM(unittest.TestCase):

    def setUp(self):
        pass

    def testTimeInWords(self):
        self.assertEqual(timeInWords(5, 47), 'thirteen minutes to six')
        self.assertEqual(timeInWords(3, 0), 'three o\' clock')
        self.assertEqual(timeInWords(7, 15), 'quarter past seven')


if __name__ == '__main__':
    unittest.main()
