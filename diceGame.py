import unittest


def countWins(dice1, dice2):
    """

    Determines the number of wins each dice has with respect to the other dice

    Inputs:
        dice1, dice2 -- list of the face numbers of the dice, size 6

    Outputs:
        number of wins for dice 1 and dice 2

    """

    assert len(dice1) == 6 and len(dice2) == 6
    dice1_wins, dice2_wins = 0, 0

    for i in dice1:
        for j in dice2:
            if i > j:
                dice1_wins += 1
            elif j > i:
                dice2_wins += 1

    return dice1_wins, dice2_wins


def findBestDice(dices):
    """

    Determines the best dice if their relation is transitive

    Inputs:
        dices -- list with lists containing the face numbers of each dice

    Output:
        the zero-based index of the best dice
        -1 if the relationship is intransitive (i.e. no best dice)

    """

    assert all(len(dice) == 6 for dice in dices)

    for i in range(len(dices)):
        wins = 0
        for j in range(len(dices)):
            dice1 = dices[i]
            dice2 = dices[j]
            a, b = countWins(dice1, dice2)
            if a > b:
                wins += 1
        if wins == len(dices) - 1:
            return i

    return -1


def findBestStrategy(dices):
    """

    Determines the strategy to follow to win the dice game

    If the relationship between the dices is transitive
    -> Choose first, pick the best dice

    If the relationship between the dices is intransitive
    -> Choose second, pick the dice that wins against the opponent's choice


    Input:
        dices -- list with lists containing the face numbers of each dice

    Output:
        strategy -- dictionary containing the entries
            choose_first --  boolean
            first_dice -- dice to pick when transitive
            1, 2, ..., n -- dice to pick when intransitive following opponents choice

    """

    assert all(len(dice) == 6 for dice in dices)

    strategy = dict()

    best_dice = findBestDice(dices)

    if best_dice == -1:
        strategy["choose_first"] = False
        for i in range(len(dices)):
            for j in range(len(dices)):
                dice1 = dices[i]
                dice2 = dices[j]
                a, b = countWins(dice1, dice2)
                if a < b:
                    strategy[i] = j

    else:
        strategy["choose_first"] = True
        strategy["first_dice"] = best_dice

    return strategy


class TestUM(unittest.TestCase):

    def setUp(self):
        pass

    def testCountWins(self):
        dice1 = [1, 2, 3, 4, 5, 6]
        dice2 = [1, 2, 3, 4, 5, 6]
        self.assertEqual(countWins(dice1, dice2), (15, 15))

        dice1 = [1, 1, 6, 6, 8, 8]
        dice2 = [2, 2, 4, 4, 9, 9]
        self.assertEqual(countWins(dice1, dice2), (16, 20))

    def testFindBestDice(self):
        self.assertEqual(findBestDice(
            [[1, 1, 6, 6, 8, 8], [2, 2, 4, 4, 9, 9], [3, 3, 5, 5, 7, 7]]), -1)
        self.assertEqual(findBestDice(
            [[1, 1, 2, 4, 5, 7], [1, 2, 2, 3, 4, 7], [1, 2, 3, 4, 5, 6]]), 2)
        self.assertEqual(findBestDice([[3, 3, 3, 3, 3, 3], [6, 6, 2, 2, 2, 2], [
                         4, 4, 4, 4, 0, 0], [5, 5, 5, 1, 1, 1]]), -1)

    def testFindBestStrategy(self):
        self.assertEqual(findBestStrategy([[1, 1, 4, 6, 7, 8], [2, 2, 2, 6, 7, 7], [
                         3, 3, 3, 5, 5, 8]]), {'choose_first': False, 0: 1, 1: 2, 2: 0})
        self.assertEqual(findBestStrategy([[4, 4, 4, 4, 0, 0], [7, 7, 3, 3, 3, 3], [
                         6, 6, 2, 2, 2, 2], [5, 5, 5, 1, 1, 1]]), {'choose_first': True, 'first_dice': 1})


if __name__ == '__main__':
    unittest.main()
