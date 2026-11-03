#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    hr = s[0:2]
    ms = s[3:8]
    ap = s[8:]
    
    if ap == 'AM' and hr == '12':
        return '00'+':'+ms
    elif ap == 'PM' and hr != '12':
        return str(int(hr)+12)+':'+ms       
    else:
        return s[0:8]

    # 01 PM ~ 12AM -> 13 ~ 00
    # 01 AM ~ 12PM -> 01 ~ 12
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
