#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    level = 0
    count = 0
    # valley = None
    # for i in range(steps):
    #     if path[i] == 'U':
    #         level += 1
    #     else:
    #         level -= 1
            
    #     if level == 0 and valley == 'IN':
    #         valley = 'OUT'
    #         count += 1
    #     elif level < 0:
    #         valley = 'IN'
        
    for step in path:
        if step == 'U':
            level += 1
            
            if level == 0:
                count += 1
        else:
            level -= 1
            
    return count
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
