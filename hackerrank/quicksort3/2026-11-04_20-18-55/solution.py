# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

def QuickSort(arr, low, high):
    if low < high:
        pivot_idx = partition(arr, low, high)
        
        sys.stdout.write(' '.join(map(str, arr)) + '\n')
        
        # exclude pivot idx, sort the left side and right side
        QuickSort(arr, low, pivot_idx-1)
        QuickSort(arr, pivot_idx+1, high)
    
def partition(arr, low, high):
    pivot = arr[low]
    small_ptr = low
    
    for i in range(low + 1, high + 1):
        if arr[i] < pivot:
            small_ptr += 1
            arr[i], arr[small_ptr] = arr[small_ptr], arr[i]
            
    arr[low], arr[small_ptr] = arr[small_ptr], arr[low]
    
    return small_ptr
    

if __name__ == '__main__':
    input_data = sys.stdin.read().strip().split()
    
    if input_data:
        n = int(input_data[0])
        arr = list(map(int, input_data[1:]))
        
        QuickSort(arr, 0, n-1)