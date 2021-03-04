'''
Find the i-th order statistic in a set of n elements, which is the i-th smallest element.
'''
def partition(arr, left, right):
    pivot = arr[right]
    i = left-1
    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            swap(arr, i, j)  # swap those smaller than pivot to left
    swap(arr, i+1, right)  # put the pivit value in the middle
    return i+1

def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]

def randomSelect(arr, i, low=None, high=None):
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
        return randomSelect(arr[low:q], i, low, q-1)
    else: 
        return randomSelect(arr[q+1:high+1], i-k, q+1, high)

if __name__ == '__main__':
    arr = [10, 4, 2, 11, 8, 9, 5, 13, 14, 12, 7, 6, 15, 1, 3]
    n = len(arr)
    i = 2
    print('The {}-th smallest element is: {}'.format(i, randomSelect(arr, i)))
    print('The top {} element is: {}'.format(n-i+1, randomSelect(arr, i)))