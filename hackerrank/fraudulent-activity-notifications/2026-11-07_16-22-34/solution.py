#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#

def activityNotifications(expenditure, d):
    # Write your code here
    
    # because 0 <= expenditure[i] <= 200, use Counting SORT!
    count = [0] * 201
    
    for i in range(d):
        count[expenditure[i]] += 1
    
    
    def twomedian(d, count):
        # d is odd
        if d % 2 == 1:
            ithnum = (d//2) + 1     # d=5 find 3th num as median
            cur_count = 0
            for val, val_count in enumerate(count):
                cur_count += val_count
                if cur_count >= ithnum:
                    return 2*val          
        # d is even
        else:
            ith1 = d//2
            ith2 = (d//2) + 1
            val1, val2 = None, None
            cur_count = 0
            for val, val_count in enumerate(count):
                cur_count += val_count
                if val1 is None and cur_count >= ith1:
                    val1 = val
                if val2 is None and cur_count >= ith2:
                    val2 = val
                    return val1 + val2 
                
        
    notice = 0
    for i in range(d, len(expenditure)):
        now_val = expenditure[i]
        if now_val >= twomedian(d, count):
            notice += 1
        
        count[now_val] += 1
        old_val = expenditure[i-d]
        count[old_val] -= 1
        
    return notice

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
