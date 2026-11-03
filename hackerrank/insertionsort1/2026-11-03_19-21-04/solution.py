#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    if not arr:
        print()
    
    # [2, 3, 4, 5, 1]
    
    # [2, 3, 4, 5, 5]
    # [2, 3, 4, 4, 5]
    # [2, 3, 3, 4, 5]
    # [2, 2, 3, 4, 5]
    # [1, 2, 3, 4, 5]
    
    target = arr[n-1]
    
    i = n-2
    while i >= 0 and arr[i] > target:
        arr[i+1] = arr[i]
        print(*arr)
        i -= 1
        
    arr[i+1] = target
    print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
