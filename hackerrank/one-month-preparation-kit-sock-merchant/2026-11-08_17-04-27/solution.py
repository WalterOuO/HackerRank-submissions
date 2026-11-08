#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#
from collections import defaultdict

def sockMerchant(n, ar):
    # Write your code here
    table = defaultdict(int)
    
    count = 0
    for a in ar:
        if table[a] != 0:
            table[a] -= 1
            count += 1
        else:
            table[a] += 1
    
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
