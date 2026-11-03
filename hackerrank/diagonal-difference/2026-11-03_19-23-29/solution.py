#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    n = len(arr)    # n could be odd, or even
    LtoR = 0
    RtoL = 0
    
    # left to right
    for i in range(n):
        LtoR += arr[i][i]
    for i in range(n-1, -1, -1):
        RtoL += arr[n-1-i][i]
    
    return abs(LtoR - RtoL)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
