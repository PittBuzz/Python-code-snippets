def samePosition(x1, v1, x2, v2):
    """

    The objects move in discrete steps at a speed of respectively v1 and v2 in the same direction (with v2 > v1).
    The objects will respectively start at x1 and x2.

    This function returns True if the two objects will be at the same position in any timestep.


    """

    if (v2 < v1):
        if ((x2 - x1) % (v2 - v1)) == 0:
            return True
        else:
            return False
    else:
        return False
