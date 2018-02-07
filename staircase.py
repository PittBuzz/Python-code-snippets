#!/bin/python3
# print a staircase of '#' of a certain height n
# input: interger
# eg. height 3
#    #
#   ##
#  ###
import sys

def staircase(n):
    for i in range(n):
        print((n-i-1)*' '+(i+1)*'#')