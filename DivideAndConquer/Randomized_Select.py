'''
Find the (i+1)-th order statistic in a set of n elements, which is the i-th smallest element.
'''
import sys
sys.path.append(r"C:\Desktop\Algos")

import Sorting.QuickSort
from Sorting.QuickSort import partition

def randomSelect(arr, low=None, high=None, i=0):
    low = 0 if low is not isinstance(low, (int, float)) else low
    high = len(arr)-1 if high is not isinstance(low, (int, float)) else high

    if low == high: 
        return arr[low]

    q = partition(arr, low, high)
    #print(arr[q])
    k = q-low+1     # the length from low to q, inclusive
    if i == k:
        return arr[q]
    if i < k:
        return randomSelect(arr[low:q], low, q-1, i)
    else: 
        return randomSelect(arr[q+1:high+1], q+1, high, i-k)

if __name__ == '__main__':
    arr = [10, 4, 2, 11, 8, 9, 5, 13, 14, 12, 7, 6, 15, 1, 3]
    i = 7
    print('The {}-th smallest element is: {}'.format(i, randomSelect(arr, i=i)))