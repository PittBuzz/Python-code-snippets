# This function returns the largest possible number obtained by rearranging a list of multiple-digit numbers


def largestNumberr(a):
    numbers = list(map(str, a))
    numbers.sort(reverse=True)
    result =  ''.join(numbers)
    
    return int(result)
