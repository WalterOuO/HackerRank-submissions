# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys
import os

def accumulatelist(arr):
    freq = [0]* 100
    
    for num in arr:
        freq[num] += 1

    cur_sum = 0
    res = []
    for i in range(100):
        cur_sum += freq[i]
        res.append(cur_sum)
    
    return res

if __name__ == '__main__':
    fptr = open(os.environ["OUTPUT_PATH"], 'w')
    
    input_data = sys.stdin.read().strip().split()

    n = int(input_data[0])
    arr = [int(input_data[i]) for i in range(1, len(input_data), 2)]

    result = accumulatelist(arr)
    
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()