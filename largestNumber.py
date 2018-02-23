def largestNumberr(a):
	"""

	This function returns the largest possible number obtained by
	rearranging a list of multiple-digit numbers

	Input:
		a -- list

	Output:
		maximal possible value

	"""

    numbers = list(map(str, a))
    numbers.sort(reverse=True)
    result = ''.join(numbers)

    return int(result)
