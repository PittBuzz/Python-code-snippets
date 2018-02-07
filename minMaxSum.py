#!/bin/python3
# Return the minimal and maximal sum that can be calculated by summing N-1 digits
#Import format: array

import sys

def minMaxSum(arr):
    som = sum(arr)
    minsom = som - max(arr)
    maxsom = som - min(arr)
    return(minsom,maxsom)