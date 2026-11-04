# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

def QuickSort(arr):
    if len(arr) <= 1:
        return arr
    p = arr[0]
    left = []
    right = []
    equal = [p]
    
    for i in range(1, len(arr)):
        if arr[i] < p:
            left.append(arr[i])
        elif arr[i] > p:
            right.append(arr[i])
        else:
            equal.append(arr[i])
        
    result = QuickSort(left) + equal + QuickSort(right)
    
    sys.stdout.write(" ".join(map(str, result)) + '\n')
    
    return result
    


if __name__ == '__main__':
    input_data = sys.stdin.read().split()
    if not input_data:
        sys.exit()
    
    n = int(input_data[0])
    arr = [int(x) for x in input_data[1: n+1] ]
    result = QuickSort(arr)
    
    