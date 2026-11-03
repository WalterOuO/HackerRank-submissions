#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
    # Write your code here
    if not arr:
        print()
    if n == 1:
        print(arr[0])
    
    for k in range(1, n):
        target = arr[k]
        i = k - 1
        while i >= 0 and target < arr[i]:
            arr[i+1] = arr[i]
            i -= 1
        
        arr[i+1] = target
        print(*arr)
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
