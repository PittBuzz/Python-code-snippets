# Take the sum of all possible combinations of m our of arr.
# This function returns the sum of all unique outcomes
# Input: array, m

from itertools import combinations
from collections import defaultdict


def iterSum(ar, m):
    sums = [sum(x) for x in combinations(ar, m)]
    d = defaultdict(int)
    for x in sums:
        d[x] += 1
    sums[:] = [x for x in sums if d[x] == 1]

    return(sum(sums))
