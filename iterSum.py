from itertools import combinations
from collections import defaultdict


def iterSum(ar, m):
	"""

	Takes the sum of all possible combinations of length m out of arr and returns the sum of all unique outcomes

	Input:
		ar -- array
		m -- length of combinations

	Output:
		sum of unique sums

	"""

    sums = [sum(x) for x in combinations(ar, m)]
    d = defaultdict(int)
    for x in sums:
        d[x] += 1
    sums[:] = [x for x in sums if d[x] == 1]

    return(sum(sums))
