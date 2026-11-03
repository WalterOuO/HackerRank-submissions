#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    numbers = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    lower_case = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
    upper_case = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'}
    special_characters = {'!','@','#','$','%','^','&','*','(',')','-','+'}
    
    count = 0
    num, low, up, spe = False, False, False, False
    for p in password:
        if p in numbers:
            num = True
        elif p in lower_case:
            low = True
        elif p in upper_case:
            up = True
        elif p in special_characters:
            spe = True
    for item in [num, low, up, spe]:
        if not item:
            count += 1

    if count + n >= 6:
        return count
    else:
        return max(6 - n, count) 
        
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
