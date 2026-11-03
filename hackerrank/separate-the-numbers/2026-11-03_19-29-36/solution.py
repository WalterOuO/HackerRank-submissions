#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def separateNumbers(s):
    # Write your code here
    s = str(s)
    
    # aleast need two number, so iterate to len(s)//2 is enough
    for l in range(len(s)//2):
        # assume the base len
        base = s[:l+1]
        if base[0] == '0':
            continue
        # mock the whole string by the base
        res = base
        i = 1
        while len(res) < len(s):
            res += str(int(base)+i)
            i += 1
        # compare with groudtruth, if not, base len +1
        if res == s:
            print('YES', base)
            return 
        
    print('NO')
            
   
        
if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
