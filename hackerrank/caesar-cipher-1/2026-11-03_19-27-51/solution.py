#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#
    # ord('z')          2 1 0
    #                 k...3
    # [a,b,c,.............x,y,z]
    #  d,e,f              a,b,c         
    
    
def caesarCipher(s, k):
    # Write your code here
    k = k % 26
    res = ''
    for w in s:
        if w.isalpha():
            if w.islower():
                res += chr( (ord(w)-ord('a')+k) %26 + ord('a') ) 
            elif w.isupper():
                res += chr( (ord(w)-ord('A')+k) %26 + ord('A') ) 
            # if w.islower():
            #     dif = ord('z') - ord(w)
            #     if dif < k:
            #         res += chr( ord('a') +  (k-1-dif) )                    
            #     else:
            #         res += chr(ord(w) + k)
            # elif w.isupper():
            #     dif = ord('Z') - ord(w)
            #     if dif < k:
            #         res += chr( ord('A') +  (k-1-dif) )                    
            #     else:
            #         res += chr(ord(w) + k)
        else:            
            res += w

    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()


