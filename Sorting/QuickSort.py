'''
Average case: O(NlgN); 

Worst case(rarely happen): O(N^2);

In place; Unstable; Use recurrence;

Used in huge amount of randomly-ordered data, need small extra space
'''
def partition(arr, left, right):
    pivot = arr[right]
    i = left-1
    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            swap(arr, i, j)  # swap those smaller than pivot to left
    swap(arr, i+1, right)  # put the pivit value in the middle
    #print(arr)
    return i+1

def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]

def quickSort(arr, left=None, right=None):
    left = 0 if not isinstance(left, (int, float)) else left
    right = len(arr)-1 if not isinstance(right, (int, float)) else right
    if left < right:
        q = partition(arr, left, right)
        quickSort(arr, left, q-1)
        quickSort(arr, q+1, right)
    return arr

if __name__ == '__main__':
    arr = [10, 4, 2, 11, 8, 9, 5, 13, 14, 12, 7, 6, 15, 1, 3]
    print('After QuickSort: ', quickSort(arr))