<<<<<<< HEAD
#!/bin/python3
# Given a time in -hour AM/PM format, convert it to military (-hour) time.
#Input format: hh:mm:ssAM
#Output format: hh:mm:ss

import sys

def timeConversion(s):
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
=======
#!/bin/python3
# Given a time in -hour AM/PM format, convert it to military (-hour) time.
#Input format: hh:mm:ssAM
#Output format: hh:mm:ss
import sys

def timeConversion(s):
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
>>>>>>> 1998b434116d641b82bb7023a888dde4eeda3960
