'''
Best case: O(N^1.3)
Average case: O(NlgN ~ N^2)
Worst case: O(N^2)

In place; Unstable
'''
def shellSort(arr):
    import math
    gap = 1
    while (gap < len(arr)/3):
        gap = gap*3 + 1
    while gap > 0:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i-gap
            while j >= 0 and arr[j] > temp:
                arr[j+gap] = arr[j]
                j -= gap
            arr[j+gap] = temp
        gap = math.floor(gap/3)
    return arr

if __name__ == '__main__':
    arr = [10, 4, 2, 11, 8, 9, 5, 13, 14, 12, 7, 6, 15, 1, 3]
    print('After shellSort: ', shellSort(arr))