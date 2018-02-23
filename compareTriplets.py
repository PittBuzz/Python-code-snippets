def compareTriplets(a0, a1, a2, b0, b1, b2)
	"""

	Given a triplet of scores, compare which participant a or b scores the highest
	for each category 0-2, the winner is awarded one point, equal score awards no points

	Input:
		a0, a1, a2 -- score of first participant
		b0, b1, b2 -- score of second participant

	Output:
		result of first and second participant


	"""

    result = [0, 0]
    if a0 > b0:
        result[0] += 1
    elif a0 < b0:
        result[1] += 1

    if a1 > b1:
        result[0] += 1
    elif a1 < b1:
        result[1] += 1

    if a2 > b2:
        result[0] += 1
    elif a2 < b2:
        result[1] += 1

    return result
