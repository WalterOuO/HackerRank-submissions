#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # Write your code here
    # s = s.lower()   # WILL COPY S, if s have 1e9 ch, will cost 1e9 space-> O(n) space
    # count = [0]*26  # spend O(1) space, fill a-z state into list
    
    # for ch in s:
    #     # not allow space by filtering using ASCII code
    #     if ord('a') <= ord(ch) <= ord('z'):
    #         count[ord(ch) - ord('a')] = 1
        
    # if count == [1]*26:
    #     return 'pangram'
    # else:
    #     return 'not pangram'
    
    seen = set()
    for ch in s:
        if ch.isalpha():
            seen.add(ch.lower())
            if len(seen) == 26:
                return 'pangram'
                
    return 'not pangram'
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
