#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    mini, maxi = 0, 0
    
    mini += min(arr)
    arr.remove(min(arr))
        
    for i in range(4):
        maxi += arr[i]
    
    arr.remove(max(arr))
    for i in range(len(arr)):
        mini += arr[i]
        
    # arr.sort()
    # for i in range(4):
    #     mini += arr[i]
    # for i in range(1, 5):
    #     maxi += arr[i]
    
    print(mini, maxi)
        

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
