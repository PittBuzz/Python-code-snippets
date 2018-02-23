def timeConversion(s):
	"""

	Given a time in -hour AM/PM format, convert it to military (-hour) time.

	Input:
		s -- string of format hh:mm:ssAM

	Output:
		string of format hh:mm:ss


	"""

    hour = s[0:2]
    halfday = s[-2:]

    if halfday == 'AM':
        if hour == '12':
            return '00' + s[2:-2]
        else:
            return s[0:-2]
    elif halfday == 'PM':
        if hour == '12':
            return s[0:-2]
        else:
            return str(int(hour) + 12) + s[2:-2]
