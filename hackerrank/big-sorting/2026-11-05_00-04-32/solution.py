#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bigSorting' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY unsorted as parameter.
#

def bigSorting(unsorted):
    # Write your code here
    
    # python function
    # return sorted(unsorted, key=lambda x: (len(x), x))
    
    
    # Merge Sort: O(nlogn) Time       
    def merge(left, right):
        merged = []
        i = k = 0
        
        while i < len(left) and k < len(right):
            # check len first, if not 
            if len(left[i]) != len(right[k]):
                condition = len(left[i]) < len(right[k])
            else:
                condition = left[i] < right[k]
            
            if condition:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[k])
                k += 1
                
        merged.extend(left[i:])
        merged.extend(right[k:])
        
        return merged 
            
    def mergesort(arr):
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        
        return merge(mergesort(left), mergesort(right))      
    
    return mergesort(unsorted)
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    unsorted = []

    for _ in range(n):
        unsorted_item = input()
        unsorted.append(unsorted_item)

    result = bigSorting(unsorted)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
