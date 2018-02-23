import sys


def minMaxSum(arr):
	"""

	Efficiently returns the minimal and maximal sum that can be calculated by summing N-1 digits

	Input:
		arr -- array

	Output:
		minimal sum
		maximal sum


	"""

    som = sum(arr)
    minsom = som - max(arr)
    maxsom = som - min(arr)
	
	return minsom, maxsom
