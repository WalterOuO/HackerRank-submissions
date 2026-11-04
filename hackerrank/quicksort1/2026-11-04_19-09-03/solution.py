#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quickSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quickSort(arr):
    # Write your code here
    # p = arr[0]
    # left = []
    # right = []
    # equal = [p]
    
    # for i in range(1, len(arr)):
    #     if arr[i] < p:
    #         left.append(arr[i])
    #     elif arr[i] > p:
    #         right.append(arr[i])
    #     else:
    #         equal.append(arr[i])
    
    # return left + equal + right
    # Evaluation
    ## Time: O(n), Space: O(n)
    
    # In-place VERSION
    def solve(low, high):
        if low >= high:
            return

        pivot = arr[low]
        left = low + 1
        right = high
        # [4, 7, 2, 6, 1, 5, 3]
        #  p  l              r
        # [4, 3, 2, 6, 1, 5, 7]
        #  p     l        r
        # [4, 3, 2, 6, 1, 5, 7]
        #  p        l  r
        # [4, 3, 2, 1, 6, 5, 7]
        #  p        r  l
        # [1, 3, 2, 4, 6, 5, 7]
        while True:
            while left <= right and arr[left] < pivot:
                left += 1
            while left <= right and arr[right] > pivot:
                right -= 1
            if left > right:
                break
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

        # when right < left, loop stop, 
        arr[low], arr[right] = arr[right], arr[low]

        ## ADD THIS to become REAL QUICKSort: recursive sort left arr, right arr
        # solve(low, right - 1)
        # solve(right + 1, high)
    solve(0, len(arr) - 1)
    return arr
    # Evaluation
    # Time: O(n), Space: O(1) In-place
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
