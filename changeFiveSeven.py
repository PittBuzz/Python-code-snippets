def changeFiveSeven(amount):
	"""

	This function itteratively returns how to pay a given amount >= 24 with coins of 5 and 7

	Input:
		amount -- integer >= 24

	Output:
		list with coins of 5 and 7

	"""


    if amount == 24:
        return [7, 7, 5, 5]
    if amount == 25:
        return [5, 5, 5, 5, 5]
    if amount == 26:
        return [7, 7, 7, 5]
    if amount == 27:
        return [7, 5, 5, 5, 5]
    if amount == 28:
        return [7, 7, 7, 7]
    else:
        result = changeFiveSeven(amount - 5)
        result.append(5)
        return result
