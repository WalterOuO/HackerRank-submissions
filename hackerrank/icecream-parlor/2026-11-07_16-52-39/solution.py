#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'icecreamParlor' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER m
#  2. INTEGER_ARRAY arr
#
from collections import defaultdict

def icecreamParlor(m, arr):
    # Write your code here
    # two sum -1
    seen = {}
    for i, val in enumerate(arr):
        needval = m - val
        if needval in seen and seen[needval] != i:
            return [seen[needval]+1, i+1]
        seen[val] = i
        
    # # two sum -2 
    # hashmap = {}
    # for i in range(len(arr)):
    #     hashmap[arr[i]] = i
    # for i in range(len(arr)):
    #     needval = m - arr[i]
    #     if needval in hashmap and hashmap[needval] != i:
    #         return [i+1, hashmap[needval] +1]
            
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        m = int(input().strip())

        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
