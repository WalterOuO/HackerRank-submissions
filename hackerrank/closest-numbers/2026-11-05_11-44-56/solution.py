#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def closestNumbers(arr):
    # Write your code here
    if len(arr) == 0 or len(arr) == 1:
        return arr
    
    arr.sort()
    res = []
    small = 1e9
    for i in range(1, len(arr)):
        if abs(arr[i-1] - arr[i]) > small:
            continue
        elif abs(arr[i-1] - arr[i]) < small:
            small = abs(arr[i] - arr[i-1])
            res = []
            
        res.append(arr[i-1])
        res.append(arr[i])
    
    return res
            
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
