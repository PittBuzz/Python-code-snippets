def plusMinus(arr):
	"""

	return the fraction of an array that is negative, positivo, and zero

	Input:
		arr -- array

	Output:
		positive fraction
		negative fraction
		zero fraction


	"""

    plus = 0
    minus = 0
    zero = 0
    n = len(arr)
    for i in range(n):
        if arr[i] > 0:
            plus += 1
        elif arr[i] < 0:
            minus += 1
        else:
            zero += 1

    return(plus / n, minus / n, zero / n)
