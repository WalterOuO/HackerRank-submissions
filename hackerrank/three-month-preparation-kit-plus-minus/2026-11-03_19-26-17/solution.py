#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    length = len(arr)
    p, n, z = 0, 0, 0
    
    for dig in arr:
        if dig > 0:
            p += 1
        elif dig < 0:
            n += 1
        else:
            z += 1
    
    for val in [p, n, z]:
        print(val/length)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
