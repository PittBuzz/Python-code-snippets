import unittest


def queensAttack(n, k, r_q, c_q, obstacles):
    """

    Counts the number of squares a queen can reach.

    Inputs:
        n -- length of the (square) bord
        k -- number of other pieces
        r_q, c_q -- position of the queen (row, column)
        obstacles -- list of list, each sublist describing the position of an other piece (row, column)

    Output:
        number of squares the queen can reach

    """

    result = 0

    obstacles = set(obstacles)

    # horizontal right
    go = True
    r_position = r_q + 1
    while go:
        if r_position > n:
            break
        if (r_position, c_q) in obstacles:
            go = False
        else:
            r_position += 1
            result += 1

    # horizontal left
    go = True
    r_position = r_q - 1
    while go:
        if r_position == 0:
            break
        if (r_position, c_q) in obstacles:
            go = False
        else:
            r_position += -1
            result += 1

    # vertical up
    go = True
    c_position = c_q + 1
    while go:
        if c_position > n:
            break
        if (r_q, c_position) in obstacles:
            go = False
        else:
            c_position += 1
            result += 1

    # vertical down
    go = True
    c_position = c_q - 1
    while go:
        if c_position == 0:
            break
        if (r_q, c_position) in obstacles:
            go = False
        else:
            c_position += -1
            result += 1

    # diagonal ++
    go = True
    c_position = c_q + 1
    r_position = r_q + 1
    while go:
        if r_position > n or c_position > n:
            break
        if (r_position, c_position) in obstacles:
            go = False
        else:
            c_position += 1
            r_position += 1
            result += 1

      # diagonal --
    go = True
    c_position = c_q - 1
    r_position = r_q - 1
    while go:
        if r_position == 0 or c_position == 0:
            break
        if (r_position, c_position) in obstacles:
            go = False
        else:
            c_position += -1
            r_position += -1
            result += 1

    # diagonal -+
    go = True
    c_position = c_q - 1
    r_position = r_q + 1
    while go:
        if r_position > n or c_position == 0:
            break
        if (r_position, c_position) in obstacles:
            go = False
        else:
            c_position += -1
            r_position += 1
            result += 1

    # diagonal +-
    go = True
    c_position = c_q + 1
    r_position = r_q - 1
    while go:
        if r_position == 0 or c_position > n:
            break
        if (r_position, c_position) in obstacles:
            go = False
        else:
            c_position += 1
            r_position += -1
            result += 1

    return result


class TestUM(unittest.TestCase):

    def setUp(self):
        pass

    def testQueensAttack(self):
        self.assertEqual(queensAttack(4, 0, 4, 4, []), 9)
        self.assertEqual(
            queensAttack(
                5, 3, 4, 3, [
                    (5, 5), (4, 2), (2, 3)]), 10)


if __name__ == '__main__':
    unittest.main()
