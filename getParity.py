def getParity(p):
	"""

	This function checks the parity of a vector

	Input:
		p -- vector

	Output:
		Boolean, return True if parity is 1

	"""

    parity = 1
    for i in range(0, len(p) - 1):
        if p[i] != i:
            parity *= -1
            mn = min(range(i, len(p)), key=p.__getitem__)
            p[i], p[mn] = p[mn], p[i]
    if parity == 1:
        return True
