#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'funnyString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def funnyString(s):
    # Write your code here
    '''
    if len(s) == 0 or len(s) == 1:
        return 'Funny'
    
    forward = []
    reverse = []
    for i in range(len(s)-1):
        forward.append(abs(ord(s[i]) - ord(s[i+1])))
        
    for i in range(len(s)-2, -1, -1):
        reverse.append(abs(ord(s[i]) - ord(s[i+1])))
    
    return 'Funny' if forward == reverse else 'Not Funny'
    # Evaluation
    ## Time: O(n), Space: O(n)
    '''
    ## Optimization: Space: O(1)

    l, r = 0, len(s) - 1
    # [0, 1]
    #  l  r
    # [0, 1, 2]
    #  l     r
    # [0, 1, 2, 3]
    #     r  l
    while l < len(s) - 1:
        if abs(ord(s[l]) - ord(s[l+1])) != abs(ord(s[r]) - ord(s[r-1])):
            return 'Not Funny'
        
        l += 1
        r -= 1
        
    return 'Funny'
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
